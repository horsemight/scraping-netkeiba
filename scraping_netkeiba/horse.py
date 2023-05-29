import logging
import re
from datetime import datetime
from typing import Optional

import pandas as pd
from bs4 import BeautifulSoup, Tag

from scraping_netkeiba import url


class Horse:
    def __init__(self, horse_id: str, html: str):
        self.__horse_id: str = horse_id
        self.__soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
        self.__horse_title: Tag = self.__soup.select_one("div.horse_title")
        self.__profile_table: Tag= self.__soup.select_one("table.db_prof_table")
        self.validate()


    def   name(self) -> str:
        return self.__horse_title.select_one("h1").text

    def eng_name(self) -> str:
        return self.__horse_title.select_one("p.eng_name").text

    def gender(self) -> str:
        horse_title_sentence: str = self.__horse_title.select_one("p.txt_01").text
        return re.match(r"^.*([牡牝セ]).*$", horse_title_sentence).group(1)

    def birth_date(self) -> datetime.date:
        birth_date_tag: Tag = self.__profile_table.find(
            "th", string="生年月日"
        ).parent.find("td")
        return datetime.strptime(birth_date_tag.text, "%Y年%m月%d日").date()

    def trainer_id(self) -> str:
        trainer_tag: Tag = (
            self.__profile_table.find("th", string="調教師").parent.find("td").find("a")
        )
        return url.trainer_pattern().match(trainer_tag.get("href")).group(1)

    def owner_id(self) -> str:
        owner_tag: Tag = (
            self.__profile_table.find("th", string="馬主").parent.find("td").find("a")
        )
        return url.owner_pattern().match(owner_tag.get("href")).group(1)

    def breeder_id(self) -> str:
        breeder_tag: Tag = (
            self.__profile_table.find("th", string="生産者").parent.find("td").find("a")
        )
        return url.breeder_pattern().match(breeder_tag.get("href")).group(1)

    def as_dataframe(self) -> pd.DataFrame:
        try:
            return pd.DataFrame.from_dict(
                {
                    "horse_id": [self.__horse_id],
                    "name": [self.name()],
                    "eng_name": [self.eng_name()],
                    "gender": [self.gender()],
                    "birth_date": [self.birth_date()],
                    "trainer_id": [self.trainer_id()],
                    "owner_id": [self.owner_id()],
                    "breeder_id": [self.breeder_id()],
                }
            )
        except Exception as e:
            logging.warning(f"An error occurred while scraping Horse: {e}")

    def validate(self):
        top: Optional[Tag] = self.__soup.find(
            "a", href=url.horse_pattern().match, attrs={"class": "active"}
        )
        if top is None:
            raise Exception("Active horse url is not found")

        top_href: str = top.get("href")
        horse_id: str = url.horse_pattern().match(top_href).group(1)
        if self.__horse_id != horse_id:
            raise Exception(
                f'Invalid horse id: expected "{self.__horse_id}", got "{horse_id}"'
            )
