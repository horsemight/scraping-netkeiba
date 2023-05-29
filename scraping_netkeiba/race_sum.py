from re import Match
from typing import List

from bs4 import BeautifulSoup, Tag

from scraping_netkeiba import url
from scraping_netkeiba.client import RaceParam


class RaceSum:
    def __init__(self, html: str):
        self.__soup = BeautifulSoup(html, "html.parser")

    def race_params(self) -> List[RaceParam]:
        race_table_tag: Tag = self.__soup.select_one("table.race_table_01")
        race_a_tags: List[Tag] = race_table_tag.find_all(
            "a", href=lambda x: url.race_patten().match(x)
        )
        race_href_matches: List[Match] = [
            url.race_patten().match(t.get("href")) for t in race_a_tags
        ]
        race_params: List[RaceParam] = [
            RaceParam(m.group(1)) for m in race_href_matches
        ]
        return race_params
