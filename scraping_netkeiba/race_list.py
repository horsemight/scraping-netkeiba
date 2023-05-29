import datetime
import re
from re import Match
from typing import List

from bs4 import BeautifulSoup, Tag

from scraping_netkeiba import url
from scraping_netkeiba.client import RaceSumParam

TITLE_PATTERN = re.compile(r"^([0-9]{4}年[0-9]{2}月[0-9]{2}日).*")


class RaceList:
    def __init__(self, race_date: datetime.date, html: str):
        self.__race_date = race_date
        self.__soup = BeautifulSoup(html, "html.parser")
        self.validate()

    def race_date(self) -> datetime.date:
        return self.__race_date

    def race_sum_params(self) -> List[RaceSumParam]:
        race_kaisai_tags: List[Tag] = self.__soup.select("div.race_kaisai")
        race_sum_a_tags: List[Tag] = [
            a
            for t in race_kaisai_tags
            for a in t.find_all("a", href=lambda x: url.race_sum_pattern().match(x))
        ]
        race_sum_hrefs: List[str] = [t.get("href") for t in race_sum_a_tags]
        race_sum_href_matches: List[Match] = [
            url.race_sum_pattern().match(v) for v in race_sum_hrefs
        ]
        race_sum_params: List[RaceSumParam] = [
            RaceSumParam(
                m.group(1), datetime.datetime.strptime(m.group(2), "%Y%m%d").date()
            )
            for m in race_sum_href_matches
        ]
        return race_sum_params

    def validate(self):
        title_tag = self.__soup.find("title")
        title_text = title_tag.text.strip()
        m: re.Match | None = re.match(r"^([0-9]{4}年[0-9]{2}月[0-9]{2}日).*", title_text)
        if not m:
            raise Exception(f"Unexpected title text: {title_text}")

        race_date = datetime.datetime.strptime(m.group(1), "%Y年%m月%d日").date()
        if self.__race_date != race_date:
            raise Exception(
                f'Invalid race date: expected "{self.__race_date}", got "{race_date}"'
            )
