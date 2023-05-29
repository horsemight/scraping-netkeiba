import enum
from typing import Optional

from bs4 import BeautifulSoup, Tag

from scraping_netkeiba import url


class Relation(enum.Enum):
    Sire = 0
    Dam = 1


class HorsePed:
    def __init__(self, horse_id: str, html: str):
        self.__horse_id = horse_id
        self.__soup = BeautifulSoup(html, "html.parser")
        self.__blood_table: Tag = self.__soup.select_one("table.blood_table")
        self.__peds: list[list[Tag]] = [
            [td for td in tr.select("td")] for tr in self.__blood_table.select("tr")
        ]
        self.validate()

    def __get_ped(self, relationships: list[Relation]) -> Tag:
        if 2 ** len(relationships) > len(self.__peds):
            raise Exception(f"Invalid relationship depth")
        tr_index = sum(
            int(len(self.__peds) / 2**i) * v.value
            for i, v in enumerate(relationships, 1)
        )
        td_index = (
            len(relationships)
            - max([i for i, v in enumerate(relationships) if v == Relation.Dam] or [0])
            - 1
        )
        return self.__peds[tr_index][td_index]

    def horse_id(self) -> str:
        return self.__horse_id

    def ped_horse_id(self, relationships: list[Relation]) -> str:
        t: Tag = self.__get_ped(relationships).find(
            "a", href=url.horse_ped_pattern().match
        )
        return url.horse_ped_pattern().match(t.get("href")).group(1)

    def sire(self) -> str:
        return self.ped_horse_id([Relation.Sire])

    def sire_sire(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Sire])

    def sire_sire_sire(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Sire, Relation.Sire])

    def sire_sire_dam(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Sire, Relation.Dam])

    def sire_dam(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Dam])

    def sire_dam_sire(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Dam, Relation.Sire])

    def sire_dam_dam(self) -> str:
        return self.ped_horse_id([Relation.Sire, Relation.Dam, Relation.Dam])

    def dam(self) -> str:
        return self.ped_horse_id([Relation.Dam])

    def dam_sire(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Sire])

    def dam_sire_sire(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Sire, Relation.Sire])

    def dam_sire_dam(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Sire, Relation.Dam])

    def dam_dam(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Dam])

    def dam_dam_sire(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Dam, Relation.Sire])

    def dam_dam_dam(self) -> str:
        return self.ped_horse_id([Relation.Dam, Relation.Dam, Relation.Dam])

    def as_dataframe(self) -> str:
        pass

    def validate(self):
        ped: Optional[Tag] = self.__soup.find(
            "a", href=url.horse_ped_pattern().match, attrs={"class": "active"}
        )
        if ped is None:
            raise Exception("Active horse url is not found")

        ped_href: str = ped.get("href")
        horse_id: str = url.horse_ped_pattern().match(ped_href).group(1)
        if self.__horse_id != horse_id:
            raise Exception(
                f'Invalid horse id: expected "{self.__horse_id}", got "{horse_id}"'
            )
