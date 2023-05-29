import logging
import re
from datetime import datetime
from enum import Enum, auto
from typing import Optional

import pandas as pd
from bs4 import BeautifulSoup, Tag

from scraping_netkeiba import url


class ScrapingExceptionCode(Enum):
    ArrivalOrder = auto()
    BracketNumber = auto()
    CornerOrders = auto()
    FinalPushTime = auto()
    HorseId = auto()
    HorseNumber = auto()
    HorseWeight = auto()
    HorseWeightDelta = auto()
    JockeyId = auto()
    LoadWeight = auto()
    PopOrder = auto()
    Prize = auto()
    TotalTime = auto()
    WinOdds = auto()
    Unknown = auto()


class ScrapingException(Exception):
    def __init__(
        self,
        message: str = "",
        code: ScrapingExceptionCode = ScrapingExceptionCode.Unknown,
        previous: Optional[Exception] = None,
    ):
        self.message = message
        self.code = code
        self.previous = previous

    def __str__(self):
        return f"[{self.code}] {self.message}: {self.previous}"


def _payoff_contents(tag: Tag, row_name: str) -> Optional[list[list[str]]]:
    if root := tag.find("th", string=lambda x: row_name in x):
        td_tags: list[Tag] = root.parent.find_all("td")
        td_contents: list[list[str]] = [
            t.decode_contents(formatter="html").split("<br/>") for t in td_tags
        ]
        td_contents: list[list[str]] = [[v.strip() for v in r] for r in td_contents]
        if td_contents[0][0] != "特":
            return td_contents


def _format_amount(x: str) -> int:
    return int(x.replace(",", ""))


class Payoff:
    def __init__(self, soup: BeautifulSoup):
        self.pay_block_tag: Tag = soup.select_one("dl.pay_block")

    def win(self) -> Optional[tuple[str, int]]:
        """単勝"""
        if contents := _payoff_contents(self.pay_block_tag, "単勝"):
            horse_nums, amounts, _ = contents
            return horse_nums[0], _format_amount(amounts[0])

    def show(self) -> Optional[list[tuple[str, int]]]:
        """複勝"""
        if contents := _payoff_contents(self.pay_block_tag, "複勝"):
            horse_nums, amounts, _ = contents
            return list(zip(horse_nums, [_format_amount(v) for v in amounts]))

    def bracket_quinella(self) -> Optional[tuple[tuple[str, str], int]]:
        """枠連"""
        if contents := _payoff_contents(self.pay_block_tag, "枠連"):
            horse_nums, amounts, _ = contents
            horse_num_tuple: list[str] = [s.strip() for s in horse_nums[0].split("-")]
            return (horse_num_tuple[0], horse_num_tuple[1]), _format_amount(amounts[0])

    def quinella(self) -> Optional[tuple[tuple[str, str], int]]:
        """馬連"""
        if contents := _payoff_contents(self.pay_block_tag, "馬連"):
            horse_nums, amounts, _ = contents
            horse_num_tuple: list[str] = [s.strip() for s in horse_nums[0].split("-")]
            return (horse_num_tuple[0], horse_num_tuple[1]), _format_amount(amounts[0])

    def quinella_place(self) -> Optional[list[tuple[tuple[str, str], int]]]:
        """ワイド"""
        if contents := _payoff_contents(self.pay_block_tag, "ワイド"):
            horse_nums, amounts, _ = contents
            horse_num_tuples: list[list[str]] = [
                [v.strip() for v in s.split("-")] for s in horse_nums
            ]
            horse_num_tuples: list[tuple[str, str]] = [
                (t[0], t[1]) for t in horse_num_tuples
            ]
            return list(zip(horse_num_tuples, [_format_amount(v) for v in amounts]))

    def exacta(self) -> Optional[tuple[tuple[str, str], int]]:
        """馬単"""
        if contents := _payoff_contents(self.pay_block_tag, "馬単"):
            horse_nums, amounts, _ = contents
            horse_num_tuple: list[str] = [
                s.strip() for s in horse_nums[0].split("&rarr;")
            ]
            return (horse_num_tuple[0], horse_num_tuple[1]), _format_amount(amounts[0])

    def trio(self) -> Optional[tuple[tuple[str, str, str], int]]:
        """三連複"""
        if contents := _payoff_contents(self.pay_block_tag, "三連複"):
            horse_nums, amounts, _ = contents
            horse_num_tuple: list[str] = [s.strip() for s in horse_nums[0].split("-")]
            return (
                horse_num_tuple[0],
                horse_num_tuple[1],
                horse_num_tuple[2],
            ), _format_amount(amounts[0])

    def trifecta(self) -> Optional[tuple[tuple[str, str, str], int]]:
        """三連単"""
        if contents := _payoff_contents(self.pay_block_tag, "三連単"):
            horse_nums, amounts, _ = contents
            horse_num_tuple: list[str] = [
                s.strip() for s in horse_nums[0].split("&rarr;")
            ]
            return (
                horse_num_tuple[0],
                horse_num_tuple[1],
                horse_num_tuple[2],
            ), _format_amount(amounts[0])


class Race:
    __spaces_pattern = re.compile(r"\s+")
    __race_info_pattern = re.compile(
        r"^(([芝ダ])(左|右|直線)\s?(外|内2周)?(\d+)m).*"
        + r"/ 天候 : (晴|曇|小雨|雨|小雪|雪).*"
        + r"/ (芝|ダート) : (良|稍重|重|不良).*"
        + r"/ 発走 : (\d{2}:\d{2}).*"
        + r"(\d{4}年\d{1,2}月\d{1,2}日).*"
        + r"\d+回(\D+)\d+日目.*$"
    )
    __horse_weight_pattern = re.compile(r"^(\d+)\((.*)\)$")

    def __init__(self, race_id: str, html: str):
        self.__race_id = race_id
        self.__soup = BeautifulSoup(html, "html.parser")

        race_num_tag: Tag = self.__soup.select_one("div.race_num")
        active_a_tag: Tag = race_num_tag.find(
            "a", href=lambda v: url.race_patten().match(v), attrs={"class": "active"}
        )
        active_href: str = active_a_tag.get("href")
        race_id_from_html: str = url.Race.parse(active_href).race_id()
        if self.__race_id != race_id_from_html:
            raise ScrapingException(
                f"Unexpected race_id: expected {race_id}, got {race_id_from_html}"
            )

        data_intro_tag: Tag = self.__soup.find("div", attrs={"class": "data_intro"})
        data_intro_p_tags: list[Tag] = data_intro_tag.find_all("p")
        race_info: str = " ".join([t.text for t in data_intro_p_tags])
        race_info: str = self.__spaces_pattern.sub(" ", race_info).strip()
        if race_info_matches := self.__race_info_pattern.match(race_info):
            self.__race_info_matches = race_info_matches
        else:
            raise ScrapingException(
                f"Unexpected race info: expected {self.__race_info_pattern.pattern}, got {race_info}"
            )

        try:
            self.__table_tag: Tag = self.__soup.find(
                "table", attrs={"class": "race_table_01", "summary": "レース結果"}
            )
            self.__tr_tags: list[Tag] = self.__table_tag.find_all("tr")
            self.__th_tags: list[Tag] = self.__tr_tags[0].find_all("th")
            self.__td_tags: list[list[Tag]] = [
                t.find_all("td") for t in self.__tr_tags[1:]
            ]
            self.__th_names: list[str] = [
                self.__spaces_pattern.sub("", e.text) for e in self.__th_tags
            ]
        except AttributeError as e:
            raise ScrapingException(previous=e)

    def payoff(self) -> Payoff:
        return Payoff(self.__soup)

    def race_id(self) -> str:
        """レースID"""
        return self.__race_id

    def race_date(self) -> datetime.date:
        """レース日"""
        return datetime.strptime(self.__race_info_matches.group(10), "%Y年%m月%d日").date()

    def post_time(self) -> datetime:
        """発走日時"""
        return datetime.combine(
            self.race_date(),
            datetime.strptime(self.__race_info_matches.group(9), "%H:%M").time(),
        )

    def weather(self) -> str:
        """天候"""
        return self.__race_info_matches.group(6)

    def racecourse(self) -> str:
        """競馬場名"""
        return self.__race_info_matches.group(11)

    def track_name(self) -> str:
        """コース名"""
        return self.__race_info_matches.group(1)

    def track_surface(self) -> str:
        """コース素材"""
        return self.__race_info_matches.group(2)

    def track_distance(self) -> int:
        """コース距離"""
        return int(self.__race_info_matches.group(5))

    def track_condition(self) -> str:
        """コース状態"""
        return self.__race_info_matches.group(8)

    def horse_count(self) -> int:
        """出走頭数"""
        return len(self.__td_tags)

    def horse_id(self) -> list[str]:
        """馬ID"""
        try:
            horse_tags: list[Tag] = [
                td_tag[self.__th_names.index("馬名")] for td_tag in self.__td_tags
            ]
            horse_a_tags: list[Tag] = [t.find("a") for t in horse_tags]
            horse_hrefs: list[str] = [t.get("href") for t in horse_a_tags]
            horse_ids: list[str] = [
                url.horse_pattern().match(v).group(1) for v in horse_hrefs
            ]
            return horse_ids
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.HorseId, previous=e)

    def jockey_id(self) -> list[str]:
        """騎手ID"""
        try:
            jockey_tags: list[Tag] = [
                td_tag[self.__th_names.index("騎手")] for td_tag in self.__td_tags
            ]
            jockey_a_tags: list[Tag] = [t.find("a") for t in jockey_tags]
            jockey_hrefs: list[str] = [t.get("href") for t in jockey_a_tags]
            jockey_ids: list[str] = [
                url.recent_jockey_result_pattern().match(v).group(1)
                for v in jockey_hrefs
            ]
            return jockey_ids
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.JockeyId, previous=e)

    def bracket_number(self) -> list[str]:
        """枠番"""
        try:
            bracket_number_tags: list[Tag] = [
                td_tag[self.__th_names.index("枠番")] for td_tag in self.__td_tags
            ]
            bracket_number_strs: list[str] = [
                t.text.strip() for t in bracket_number_tags
            ]
            return bracket_number_strs
        except Exception as e:
            raise ScrapingException(
                code=ScrapingExceptionCode.BracketNumber, previous=e
            )

    def horse_number(self) -> list[str]:
        """馬番"""
        try:
            horse_number_tags: list[Tag] = [
                td_tag[self.__th_names.index("馬番")] for td_tag in self.__td_tags
            ]
            horse_number_strs: list[str] = [t.text.strip() for t in horse_number_tags]
            return horse_number_strs
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.HorseNumber, previous=e)

    def corner_orders(self) -> list[str]:
        """通過順"""
        try:
            corner_orders_tags: list[Tag] = [
                td_tag[self.__th_names.index("通過")] for td_tag in self.__td_tags
            ]
            corner_orders: list[str] = [t.text.strip() for t in corner_orders_tags]
            return corner_orders
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.CornerOrders, previous=e)

    def arrival_order(self) -> list[str]:
        """着順"""
        try:
            arrival_order_tags: list[Tag] = [
                td_tag[self.__th_names.index("着順")] for td_tag in self.__td_tags
            ]
            arrival_orders: list[str] = [t.text.strip() for t in arrival_order_tags]
            return arrival_orders
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.ArrivalOrder, previous=e)

    def pop_order(self) -> list[str]:
        """人気順"""
        try:
            pop_order_tags: list[Tag] = [
                td_tag[self.__th_names.index("人気")] for td_tag in self.__td_tags
            ]
            pop_orders: list[str] = [t.text.strip() for t in pop_order_tags]
            return pop_orders
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.PopOrder, previous=e)

    def horse_weight_text(self) -> list[str]:
        """馬体重（文字列）"""
        try:
            horse_weight_tags: list[Tag] = [
                td_tag[self.__th_names.index("馬体重")] for td_tag in self.__td_tags
            ]
            horse_weight_texts: list[str] = [t.text.strip() for t in horse_weight_tags]
            return horse_weight_texts
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.HorseWeight, previous=e)

    def horse_weight(self) -> list[Optional[float]]:
        """馬体重"""

        def to_float(val: str) -> Optional[float]:
            if val in ["", "計不"]:
                return None
            else:
                if m := self.__horse_weight_pattern.match(val):
                    return float(m.group(1))
                else:
                    logging.warning(f"Unexpected horse weight value: {val}")
                    print(f"Unexpected horse weight value: {val}")
                    return None

        try:
            horse_weights: list[Optional[float]] = [
                to_float(s) for s in self.horse_weight_text()
            ]
            return horse_weights
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.HorseWeight, previous=e)

    def horse_weight_delta(self) -> list[Optional[float]]:
        """馬体重変動"""

        def to_float(val: str) -> Optional[float]:
            if val in ["", "計不"]:
                return None
            else:
                if m := self.__horse_weight_pattern.match(val):
                    return float(m.group(2))
                else:
                    logging.warning(f"Unexpected horse weight value: {val}")
                    return None

        try:
            horse_weight_deltas: list[Optional[float]] = [
                to_float(s) for s in self.horse_weight_text()
            ]
            return horse_weight_deltas
        except Exception as e:
            raise ScrapingException(
                code=ScrapingExceptionCode.HorseWeightDelta, previous=e
            )

    def load_weight(self) -> list[Optional[float]]:
        """斤量"""

        def to_float(val: str) -> float:
            return None if val == "" else float(val)

        try:
            load_weight_tags: list[Tag] = [
                td_tag[self.__th_names.index("斤量")] for td_tag in self.__td_tags
            ]
            load_weights: list[str] = [t.text.strip() for t in load_weight_tags]
            load_weights: list[Optional[float]] = [to_float(s) for s in load_weights]
            return load_weights
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.LoadWeight, previous=e)

    def total_time(self) -> list[Optional[float]]:
        """総合タイム"""

        def to_float(val: str) -> Optional[float]:
            if val == "":
                return None
            else:
                l = val.split(":")
                return float(l[0]) * 60 + float(l[1])

        try:
            total_time_tags: list[Tag] = [
                td_tag[self.__th_names.index("タイム")] for td_tag in self.__td_tags
            ]
            total_times: list[str] = [t.text.strip() for t in total_time_tags]
            total_times: list[Optional[float]] = [to_float(s) for s in total_times]
            return total_times
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.TotalTime, previous=e)

    def final_push_time(self) -> list[Optional[float]]:
        """上りタイム"""

        def to_float(val: str) -> Optional[float]:
            return None if val == "" else float(val)

        try:
            final_push_time_tags: list[Tag] = [
                td_tag[self.__th_names.index("上り")] for td_tag in self.__td_tags
            ]
            final_push_times: list[str] = [t.text.strip() for t in final_push_time_tags]
            final_push_times: list[Optional[float]] = [
                to_float(s) for s in final_push_times
            ]
            return final_push_times
        except Exception as e:
            raise ScrapingException(
                code=ScrapingExceptionCode.FinalPushTime, previous=e
            )

    def win_odds(self) -> list[Optional[float]]:
        """単勝オッズ"""

        def to_float(val: str) -> Optional[float]:
            return None if val in ["", "---"] else float(val)

        try:
            win_odds_tags: list[Tag] = [
                td_tag[self.__th_names.index("単勝")] for td_tag in self.__td_tags
            ]
            win_odds: list[str] = [t.text.strip() for t in win_odds_tags]
            win_odds: list[Optional[float]] = [to_float(s) for s in win_odds]
            return win_odds
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.WinOdds, previous=e)

    def prize(self) -> list[int]:
        """賞金（円）"""

        def to_int(val: str) -> int:
            val = val.replace(",", "")
            return 0 if val == "" else int(float(val) * 1000000)

        try:
            prize_tags: list[Tag] = [
                td_tag[self.__th_names.index("賞金(万円)")] for td_tag in self.__td_tags
            ]
            prizes: list[str] = [t.text.strip() for t in prize_tags]
            prizes: list[int] = [to_int(s) for s in prizes]
            return prizes
        except Exception as e:
            raise ScrapingException(code=ScrapingExceptionCode.Prize, previous=e)

    def race_info_as_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(
            {
                "race_id": [self.race_id()],
                "race_date": [self.race_date()],
                "post_time": [self.post_time()],
                "weather": [self.weather()],
                "racecourse": [self.racecourse()],
                "track_name": [self.track_name()],
                "track_surface": [self.track_surface()],
                "track_distance": [self.track_distance()],
                "track_condition": [self.track_condition()],
                "horse_count": [self.horse_count()],
            }
        )

    def race_result_as_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(
            {
                "race_id": [self.race_id()] * self.horse_count(),
                "horse_id": self.horse_id(),
                "jockey_id": self.jockey_id(),
                "bracket_number": self.bracket_number(),
                "horse_number": self.horse_number(),
                "corner_orders": self.corner_orders(),
                "arrival_order": self.arrival_order(),
                "pop_order": self.pop_order(),
                "horse_weight": self.horse_weight(),
                "load_weight": self.load_weight(),
                "time": self.total_time(),
                "final_push_time": self.final_push_time(),
                "win_odds": self.win_odds(),
                "prize": self.prize(),
            }
        )
