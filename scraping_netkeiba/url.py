import datetime
import re
from functools import cache
from typing import Self, Union
from urllib.parse import urlencode, urlparse, urlunparse

BASE_URL = "https://db.netkeiba.com"


def _assert_pattern(pattern: re.Pattern, string: str) -> str:
    if pattern.match(string):
        return string
    raise ValueError(
        'Unexpected URL path pattern: expected "{}", got "{}"'.format(
            pattern.pattern, string
        )
    )


def _match_pattern(pattern: re.Pattern, string: str) -> re.Match:
    if m := pattern.match(string):
        return m
    raise ValueError(
        'Unexpected URL path pattern: expected "{}", got "{}"'.format(
            pattern.pattern, string
        )
    )


def _generate(path: str, params: dict[str, Union[str, int, float]] = None) -> str:
    url = list(urlparse(BASE_URL))
    url[2] = path
    url[4] = urlencode(params) if params else ""
    return urlunparse(url)


class Race:
    __race_id_pattern: re.Pattern = re.compile(r"[a-zA-Z0-9]{12}")
    __url_pattern: re.Pattern = re.compile(rf"/race/({__race_id_pattern.pattern})/")

    @classmethod
    def parse(cls, url: str) -> Self:
        m = _match_pattern(cls.__url_pattern, url.replace(BASE_URL, ""))
        return Race(m.group(1))

    def __init__(self, race_id: str):
        self.__race_id: str = _assert_pattern(self.__race_id_pattern, race_id)

    def race_id(self) -> str:
        return self.__race_id

    def generate(self) -> str:
        return _generate(f"/race/{self.__race_id}/")


@cache
def race_patten() -> re.Pattern:
    return re.compile(r"/race/([a-zA-Z0-9]{12})/")


def race(race_id: str) -> str:
    return _generate(_assert_pattern(race_patten(), f"/race/{race_id}/"))


@cache
def race_list_patten() -> re.Pattern:
    return re.compile(r"/race/list/([0-9]{8})/")


def race_list(date: datetime.date) -> str:
    return _generate(
        _assert_pattern(race_list_patten(), f'/race/list/{date.strftime("%Y%m%d")}/')
    )


@cache
def race_sum_pattern() -> re.Pattern:
    return re.compile(r"/race/sum/([0-9]{2})/([0-9]{8})/")


def race_sum(track_id: str, date: datetime.date) -> str:
    return _generate(
        _assert_pattern(
            race_sum_pattern(), f'/race/sum/{track_id}/{date.strftime("%Y%m%d")}/'
        )
    )


@cache
def horse_pattern() -> re.Pattern:
    return re.compile(r"/horse/([a-zA-Z0-9]{10})/")


def horse(horse_id: str) -> str:
    return _generate(_assert_pattern(horse_pattern(), f"/horse/{horse_id}/"))


@cache
def horse_result_pattern() -> re.Pattern:
    return re.compile(r"/horse/result/([a-zA-Z0-9]{10})/")


def horse_result(horse_id: str) -> str:
    return _generate(
        _assert_pattern(horse_result_pattern(), f"/horse/result/{horse_id}/")
    )


@cache
def horse_ped_pattern() -> re.Pattern:
    return re.compile(r"/horse/ped/([a-zA-Z0-9]{10})/")


def horse_ped(horse_id: str) -> str:
    return _generate(_assert_pattern(horse_ped_pattern(), f"/horse/ped/{horse_id}/"))


@cache
def breeder_pattern() -> re.Pattern:
    return re.compile(r"/breeder/([a-zA-Z0-9]{6})/")


def breeder(breeder_id: str) -> str:
    return _generate(_assert_pattern(breeder_pattern(), f"/breeder/{breeder_id}/"))


@cache
def owner_pattern() -> re.Pattern:
    return re.compile(r"/owner/([a-zA-Z0-9]{6})/")


def owner(owner_id: str) -> str:
    return _generate(_assert_pattern(owner_pattern(), f"/owner/{owner_id}/"))


@cache
def trainer_pattern() -> re.Pattern:
    return re.compile(r"/trainer/([a-zA-Z0-9]{5})/")


def trainer(trainer_id: str) -> str:
    return _generate(_assert_pattern(trainer_pattern(), f"/trainer/{trainer_id}/"))


@cache
def recent_jockey_result_pattern() -> re.Pattern:
    return re.compile(r"/jockey/result/recent/([a-zA-Z0-9]{5})/")


def recent_jockey_result(jockey_id: str) -> str:
    return _generate(
        _assert_pattern(
            recent_jockey_result_pattern(), f"/jockey/result/recent/{jockey_id}/"
        )
    )


def parse(path: str) -> str:
    patterns = [
        breeder_pattern(),
        horse_pattern(),
        horse_ped_pattern(),
        horse_result_pattern(),
        owner_pattern(),
        race_sum_pattern(),
        trainer_pattern(),
    ]
    for p in patterns:
        if p.match(path):
            return _generate(path)
    raise ValueError(f"Unsupported URL path: {path}")
