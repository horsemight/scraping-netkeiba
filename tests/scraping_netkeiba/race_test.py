import datetime
import os.path
from pathlib import Path
from typing import Optional

import pytest

from scraping_netkeiba.race import Race, ScrapingException

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize(
    "path",
    [
        script_dir / "data/race/2021N2a00905.html",
        script_dir / "data/race/202165122904.html",
    ],
)
def test_init_raises_exception(path: Path):
    race_id = path.stem
    with pytest.raises(ScrapingException) as _:
        Race(race_id, path.read_text())


@pytest.mark.parametrize(
    "path",
    [
        script_dir / "data/race/202102011201.html",
        script_dir / "data/race/202105010101.html",
        script_dir / "data/race/202106050907.html",
        script_dir / "data/race/202136123104.html",
        script_dir / "data/race/202142122408.html",
        script_dir / "data/race/202144123104.html",
        script_dir / "data/race/202147123109.html",
        script_dir / "data/race/202150122910.html",
    ],
)
def test_race_id(path: Path):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.race_id() == race_id


@pytest.mark.parametrize(
    "path, race_date",
    [
        [script_dir / "data/race/202102011201.html", datetime.date(2021, 8, 8)],
        [script_dir / "data/race/202105010101.html", datetime.date(2021, 1, 30)],
        [script_dir / "data/race/202106050907.html", datetime.date(2021, 12, 28)],
        [script_dir / "data/race/202136123104.html", datetime.date(2021, 12, 31)],
        [script_dir / "data/race/202142122408.html", datetime.date(2021, 12, 24)],
        [script_dir / "data/race/202144123104.html", datetime.date(2021, 12, 31)],
        [script_dir / "data/race/202147123109.html", datetime.date(2021, 12, 31)],
        [script_dir / "data/race/202150122910.html", datetime.date(2021, 12, 29)],
    ],
)
def test_race_date(path: Path, race_date: datetime.date):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.race_date() == race_date


@pytest.mark.parametrize(
    "path, post_time",
    [
        [
            script_dir / "data/race/202102011201.html",
            datetime.datetime(2021, 8, 8, 9, 55),
        ],
        [
            script_dir / "data/race/202105010101.html",
            datetime.datetime(2021, 1, 30, 10, 10),
        ],
        [
            script_dir / "data/race/202106050907.html",
            datetime.datetime(2021, 12, 28, 13, 5),
        ],
        [
            script_dir / "data/race/202136123104.html",
            datetime.datetime(2021, 12, 31, 12, 20),
        ],
        [
            script_dir / "data/race/202142122408.html",
            datetime.datetime(2021, 12, 24, 13, 50),
        ],
        [
            script_dir / "data/race/202144123104.html",
            datetime.datetime(2021, 12, 31, 12, 40),
        ],
        [
            script_dir / "data/race/202147123109.html",
            datetime.datetime(2021, 12, 31, 15, 20),
        ],
        [
            script_dir / "data/race/202150122910.html",
            datetime.datetime(2021, 12, 29, 15, 25),
        ],
    ],
)
def test_post_time(path: Path, post_time: datetime.datetime):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.post_time() == post_time


@pytest.mark.parametrize(
    "path, weather",
    [
        [script_dir / "data/race/202102011201.html", "曇"],
        [script_dir / "data/race/202105010101.html", "晴"],
        [script_dir / "data/race/202106050907.html", "晴"],
        [script_dir / "data/race/202136123104.html", "小雪"],
        [script_dir / "data/race/202142122408.html", "晴"],
        [script_dir / "data/race/202144123104.html", "曇"],
        [script_dir / "data/race/202147123109.html", "雪"],
        [script_dir / "data/race/202150122910.html", "曇"],
    ],
)
def test_weather(path: Path, weather: str):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.weather() == weather


@pytest.mark.parametrize(
    "path, racecourse",
    [
        [script_dir / "data/race/202102011201.html", "函館"],
        [script_dir / "data/race/202105010101.html", "東京"],
        [script_dir / "data/race/202106050907.html", "中山"],
        [script_dir / "data/race/202136123104.html", "水沢"],
        [script_dir / "data/race/202142122408.html", "浦和"],
        [script_dir / "data/race/202144123104.html", "大井"],
        [script_dir / "data/race/202147123109.html", "笠松"],
        [script_dir / "data/race/202150122910.html", "園田"],
    ],
)
def test_racecourse(path: Path, racecourse: str):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.racecourse() == racecourse


@pytest.mark.parametrize(
    "path, track_name",
    [
        [script_dir / "data/race/202102011201.html", "ダ右1700m"],
        [script_dir / "data/race/202105010101.html", "ダ左1400m"],
        [script_dir / "data/race/202106050907.html", "芝右2000m"],
        [script_dir / "data/race/202136123104.html", "ダ右1300m"],
        [script_dir / "data/race/202142122408.html", "ダ左1400m"],
        [script_dir / "data/race/202144123104.html", "ダ右1400m"],
        [script_dir / "data/race/202147123109.html", "ダ右1600m"],
        [script_dir / "data/race/202150122910.html", "ダ右1700m"],
    ],
)
def test_track_name(path: Path, track_name: str):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.track_name() == track_name


@pytest.mark.parametrize(
    "path, track_surface",
    [
        [script_dir / "data/race/202102011201.html", "ダ"],
        [script_dir / "data/race/202105010101.html", "ダ"],
        [script_dir / "data/race/202106050907.html", "芝"],
        [script_dir / "data/race/202136123104.html", "ダ"],
        [script_dir / "data/race/202142122408.html", "ダ"],
        [script_dir / "data/race/202144123104.html", "ダ"],
        [script_dir / "data/race/202147123109.html", "ダ"],
        [script_dir / "data/race/202150122910.html", "ダ"],
    ],
)
def test_track_surface(path: Path, track_surface: str):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.track_surface() == track_surface


@pytest.mark.parametrize(
    "path, track_distance",
    [
        [script_dir / "data/race/202102011201.html", 1700],
        [script_dir / "data/race/202105010101.html", 1400],
        [script_dir / "data/race/202106050907.html", 2000],
        [script_dir / "data/race/202136123104.html", 1300],
        [script_dir / "data/race/202142122408.html", 1400],
        [script_dir / "data/race/202144123104.html", 1400],
        [script_dir / "data/race/202147123109.html", 1600],
        [script_dir / "data/race/202150122910.html", 1700],
    ],
)
def test_track_distance(path: Path, track_distance: int):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.track_distance() == track_distance


@pytest.mark.parametrize(
    "path, horse_count",
    [
        [script_dir / "data/race/202102011201.html", 14],
        [script_dir / "data/race/202105010101.html", 16],
        [script_dir / "data/race/202106050907.html", 16],
        [script_dir / "data/race/202136123104.html", 8],
        [script_dir / "data/race/202142122408.html", 12],
        [script_dir / "data/race/202144123104.html", 12],
        [script_dir / "data/race/202147123109.html", 9],
        [script_dir / "data/race/202150122910.html", 12],
    ],
)
def test_horse_count(path: Path, horse_count: int):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.horse_count() == horse_count


@pytest.mark.parametrize(
    "path, horse_id",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                "2019101479",
                "2019100800",
                "2019104010",
                "2019104953",
                "2019110083",
                "2019103937",
                "2019106008",
                "2019102433",
                "2019102483",
                "2019102459",
                "2019106340",
                "2019101093",
                "2019106700",
                "2019103643",
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "2018105460",
                "2018101711",
                "2018104480",
                "2018100299",
                "2018100601",
                "2018101484",
                "2018100688",
                "2018101965",
                "2018103840",
                "2018101424",
                "2018102840",
                "2018106320",
                "2018100689",
                "2018100498",
                "2018102435",
                "2018101552",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "2017104903",
                "2016102615",
                "2018104711",
                "2017101556",
                "2017102100",
                "2018104827",
                "2015101835",
                "2016104238",
                "2018103018",
                "2016104523",
                "2016101404",
                "2018100592",
                "2017105978",
                "2018103429",
                "2017110150",
                "2015106231",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [
                "2018100100",
                "2018106656",
                "2017102821",
                "2018103835",
                "2018100038",
                "2018102540",
                "2016104207",
                "2018102187",
            ],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [
                "2017100292",
                "2016103445",
                "2016106517",
                "2014104229",
                "2014110034",
                "2015101819",
                "2015101801",
                "2017101096",
                "2013101853",
                "2017103029",
                "2014101283",
                "2017102455",
            ],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [
                "2019104566",
                "2019102405",
                "2019102426",
                "2019104181",
                "2019101991",
                "2019104559",
                "2019100116",
                "2019100892",
                "2019101600",
                "2019105577",
                "2019102390",
                "2019103075",
            ],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [
                "2013105192",
                "2015106102",
                "2014102185",
                "2014110023",
                "2016104312",
                "2017106336",
                "2014100082",
                "2017106585",
                "2014103037",
            ],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [
                "2017102930",
                "2016106106",
                "2016105708",
                "2017106535",
                "2016100895",
                "2017102021",
                "2015102611",
                "2018100628",
                "2016104184",
                "2016104188",
                "2018102514",
                "2016101987",
            ],
        ],
    ],
)
def test_horse_id(path: Path, horse_id: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.horse_id() == horse_id


@pytest.mark.parametrize(
    "path, jockey_id",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                "01140",
                "01091",
                "01189",
                "01096",
                "05203",
                "01108",
                "01177",
                "01182",
                "01025",
                "01018",
                "01185",
                "01180",
                "01181",
                "01109",
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "05386",
                "01170",
                "01117",
                "01075",
                "01096",
                "00422",
                "01122",
                "01184",
                "01135",
                "01134",
                "01029",
                "00733",
                "01150",
                "01092",
                "01158",
                "01108",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "05604",
                "01173",
                "01179",
                "01184",
                "01183",
                "01189",
                "01185",
                "05609",
                "05608",
                "01167",
                "01187",
                "05611",
                "05607",
                "01181",
                "01186",
                "05605",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["a01d1", "05463", "a03fd", "05462", "05490", "05294", "05552", "05577"],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [
                "a02c4",
                "05001",
                "a0233",
                "a01f3",
                "05248",
                "05553",
                "05397",
                "a02c3",
                "05611",
                "05348",
                "a017e",
                "a017d",
            ],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [
                "05404",
                "a02ad",
                "05559",
                "05540",
                "05549",
                "05342",
                "05590",
                "05524",
                "05380",
                "a025f",
                "a0277",
                "05583",
            ],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [
                "05171",
                "a0162",
                "00410",
                "a02e0",
                "05521",
                "05489",
                "a0422",
                "a0032",
                "a03df",
            ],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [
                "05530",
                "05217",
                "a0395",
                "a01e6",
                "05328",
                "a0488",
                "05597",
                "05390",
                "05616",
                "a029e",
                "a01bb",
                "05545",
            ],
        ],
    ],
)
def test_jockey_id(path: Path, jockey_id: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.jockey_id() == jockey_id


@pytest.mark.parametrize(
    "path, bracket_number",
    [
        [
            script_dir / "data/race/202102011201.html",
            ["5", "5", "8", "4", "6", "4", "2", "7", "3", "6", "8", "7", "3", "1"],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "1",
                "2",
                "2",
                "4",
                "6",
                "8",
                "5",
                "7",
                "8",
                "1",
                "3",
                "6",
                "5",
                "3",
                "4",
                "7",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "4",
                "5",
                "6",
                "8",
                "7",
                "5",
                "8",
                "6",
                "2",
                "3",
                "4",
                "7",
                "1",
                "3",
                "1",
                "2",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["1", "2", "3", "4", "5", "6", "7", "8"],
        ],
        [
            script_dir / "data/race/202142122408.html",
            ["6", "8", "8", "3", "2", "7", "6", "5", "1", "4", "7", "5"],
        ],
        [
            script_dir / "data/race/202144123104.html",
            ["6", "2", "5", "1", "5", "8", "7", "7", "3", "4", "6", "8"],
        ],
        [
            script_dir / "data/race/202147123109.html",
            ["7", "8", "2", "3", "4", "5", "6", "1", "8"],
        ],
        [
            script_dir / "data/race/202150122910.html",
            ["7", "5", "6", "2", "5", "4", "8", "6", "8", "3", "7", "1"],
        ],
    ],
)
def test_bracket_number(path: Path, bracket_number: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.bracket_number() == bracket_number


@pytest.mark.parametrize(
    "path, horse_number",
    [
        [
            script_dir / "data/race/202102011201.html",
            ["7", "8", "13", "6", "9", "5", "2", "11", "3", "10", "14", "12", "4", "1"],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "2",
                "4",
                "3",
                "8",
                "12",
                "16",
                "10",
                "13",
                "15",
                "1",
                "6",
                "11",
                "9",
                "5",
                "7",
                "14",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "7",
                "9",
                "11",
                "15",
                "13",
                "10",
                "16",
                "12",
                "3",
                "6",
                "8",
                "14",
                "1",
                "5",
                "2",
                "4",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["1", "2", "3", "4", "5", "6", "7", "8"],
        ],
        [
            script_dir / "data/race/202142122408.html",
            ["8", "11", "12", "3", "2", "9", "7", "5", "1", "4", "10", "6"],
        ],
        [
            script_dir / "data/race/202144123104.html",
            ["8", "2", "6", "1", "5", "11", "9", "10", "3", "4", "7", "12"],
        ],
        [
            script_dir / "data/race/202147123109.html",
            ["7", "9", "2", "3", "4", "5", "6", "1", "8"],
        ],
        [
            script_dir / "data/race/202150122910.html",
            ["9", "6", "8", "2", "5", "4", "12", "7", "11", "3", "10", "1"],
        ],
    ],
)
def test_horse_number(path: Path, horse_number: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.horse_number() == horse_number


@pytest.mark.parametrize(
    "path, corner_orders",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                "1-1-1-1",
                "5-4-3-3",
                "2-2-2-2",
                "14-14-13-9",
                "12-12-10-6",
                "5-7-5-5",
                "11-8-6-6",
                "13-13-11-9",
                "9-8-6-6",
                "2-2-3-4",
                "9-8-11-12",
                "4-4-8-11",
                "5-6-8-12",
                "8-8-13-14",
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "1-1",
                "7-7",
                "2-2",
                "3-3",
                "4-5",
                "4-3",
                "4-5",
                "14-13",
                "7-7",
                "10-9",
                "15-14",
                "12-11",
                "11-11",
                "9-9",
                "12-14",
                "16-16",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "6-6-5-4",
                "4-4-7-7",
                "8-8-8-6",
                "4-4-2-2",
                "10-10-5-5",
                "3-3-2-1",
                "2-2-1-2",
                "14-14-11-10",
                "8-8-8-9",
                "16-16-15-14",
                "1-1-4-7",
                "12-12-11-11",
                "10-11-13-12",
                "12-13-14-14",
                "6-7-10-12",
                "15-15-16",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["", "", "", "", "", "", "", ""],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [
                "3-4-2-2",
                "2-2-1-1",
                "6-7-6-5",
                "4-3-4-4",
                "10-8-11-9",
                "9-9-8-6",
                "7-6-7-8",
                "8-10-9-10",
                "1-1-3-3",
                "5-5-5-7",
                "11-11-10-11",
                "12-12-12-12",
            ],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [
                "5-3-3",
                "10-10-10",
                "1-1-1",
                "8-9-7",
                "4-8-8",
                "7-4-5",
                "2-2-2",
                "9-7-9",
                "3-5-4",
                "11-11-11",
                "6-6-6",
                "",
            ],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [
                "2-1-1",
                "8-5-5",
                "3-3-3",
                "7-6-6",
                "6-4-3",
                "1-2-2",
                "5-7-7",
                "4-8-8",
                "",
            ],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [
                "5-5-4-3",
                "10-10-4-6",
                "11-11-11-11",
                "4-4-4-3",
                "6-6-8-7",
                "1-1-1-1",
                "8-6-7-8",
                "2-2-2-2",
                "6-8-9-9",
                "9-9-10-9",
                "3-3-3-5",
                "",
            ],
        ],
    ],
)
def test_corner_orders(path: Path, corner_orders: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.corner_orders() == corner_orders


@pytest.mark.parametrize(
    "path, arrival_order",
    [
        [
            script_dir / "data/race/202102011201.html",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "中",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["", "", "", "", "", "", "", ""],
        ],
        [
            script_dir / "data/race/202142122408.html",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        ],
        [
            script_dir / "data/race/202144123104.html",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "取"],
        ],
        [
            script_dir / "data/race/202147123109.html",
            ["1", "2", "3", "4", "5", "6", "7", "8", "除"],
        ],
        [
            script_dir / "data/race/202150122910.html",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "除"],
        ],
    ],
)
def test_arrival_order(path: Path, arrival_order: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.arrival_order() == arrival_order


@pytest.mark.parametrize(
    "path, pop_order",
    [
        [
            script_dir / "data/race/202102011201.html",
            ["1", "2", "5", "8", "4", "7", "6", "12", "9", "3", "14", "11", "13", "10"],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                "5",
                "2",
                "3",
                "1",
                "6",
                "7",
                "4",
                "12",
                "13",
                "15",
                "8",
                "10",
                "9",
                "11",
                "14",
                "16",
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                "11",
                "12",
                "1",
                "2",
                "3",
                "4",
                "10",
                "7",
                "6",
                "9",
                "8",
                "13",
                "16",
                "14",
                "15",
                "5",
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            ["", "", "", "", "", "", "", ""],
        ],
        [
            script_dir / "data/race/202142122408.html",
            ["2", "10", "4", "1", "7", "12", "6", "5", "8", "3", "9", "11"],
        ],
        [
            script_dir / "data/race/202144123104.html",
            ["1", "4", "7", "8", "5", "3", "11", "9", "2", "6", "10", ""],
        ],
        [
            script_dir / "data/race/202147123109.html",
            ["2", "5", "6", "3", "1", "4", "7", "8", ""],
        ],
        [
            script_dir / "data/race/202150122910.html",
            ["8", "1", "10", "9", "7", "3", "4", "2", "5", "11", "6", ""],
        ],
    ],
)
def test_pop_order(path: Path, pop_order: list[str]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.pop_order() == pop_order


@pytest.mark.parametrize(
    "path, horse_weight",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                494.0,
                442.0,
                448.0,
                472.0,
                492.0,
                482.0,
                480.0,
                474.0,
                476.0,
                524.0,
                456.0,
                430.0,
                470.0,
                476.0,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                468.0,
                460.0,
                462.0,
                432.0,
                420.0,
                432.0,
                454.0,
                454.0,
                474.0,
                462.0,
                498.0,
                500.0,
                432.0,
                434.0,
                432.0,
                404.0,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                534.0,
                472.0,
                448.0,
                506.0,
                480.0,
                476.0,
                462.0,
                458.0,
                492.0,
                426.0,
                480.0,
                466.0,
                460.0,
                486.0,
                532.0,
                506.0,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [420.0, 445.0, 520.0, 454.0, 452.0, 486.0, 479.0, 464.0],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [
                439.0,
                490.0,
                435.0,
                462.0,
                486.0,
                435.0,
                446.0,
                460.0,
                485.0,
                486.0,
                479.0,
                489.0,
            ],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [
                469.0,
                466.0,
                489.0,
                434.0,
                463.0,
                463.0,
                447.0,
                486.0,
                401.0,
                509.0,
                424.0,
                None,
            ],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [490.0, 530.0, 534.0, 472.0, 491.0, 449.0, 518.0, 533.0, None],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [
                509.0,
                478.0,
                480.0,
                497.0,
                509.0,
                454.0,
                507.0,
                460.0,
                423.0,
                485.0,
                449.0,
                467.0,
            ],
        ],
    ],
)
def test_horse_weight(path: Path, horse_weight: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.horse_weight() == horse_weight


@pytest.mark.parametrize(
    "path, horse_weight_delta",
    [
        [
            script_dir / "data/race/202102011201.html",
            [6.0, 4.0, 0.0, 4.0, 2.0, 2.0, 0.0, 4.0, 8.0, 16.0, 2.0, -6.0, 0.0, -2.0],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                -4.0,
                4.0,
                2.0,
                0.0,
                -2.0,
                -4.0,
                0.0,
                8.0,
                14.0,
                12.0,
                22.0,
                6.0,
                6.0,
                -12.0,
                -2.0,
                26.0,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                8.0,
                0.0,
                4.0,
                10.0,
                6.0,
                8.0,
                -2.0,
                2.0,
                22.0,
                6.0,
                -8.0,
                24.0,
                18.0,
                16.0,
                4.0,
                -4.0,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [1.0, 0.0, 33.0, -2.0, 6.0, 1.0, 1.0, 4.0],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [-7.0, -2.0, 0.0, 4.0, 14.0, -3.0, -3.0, -9.0, -6.0, -6.0, -16.0, 1.0],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [5.0, -1.0, 2.0, 6.0, -7.0, -4.0, 2.0, -3.0, -5.0, 13.0, -6.0, None],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [-1.0, 7.0, 2.0, 5.0, -1.0, -1.0, 1.0, 18.0, None],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [-4.0, -3.0, 1.0, -2.0, 0.0, 2.0, 1.0, -1.0, -5.0, 3.0, 0.0, 2.0],
        ],
    ],
)
def test_horse_weight_delta(path: Path, horse_weight_delta: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.horse_weight_delta() == horse_weight_delta


@pytest.mark.parametrize(
    "path, load_weight",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                54.0,
                54.0,
                51.0,
                54.0,
                54.0,
                54.0,
                51.0,
                53.0,
                54.0,
                54.0,
                51.0,
                54.0,
                52.0,
                54.0,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                51.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
                54.0,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                57.0,
                57.0,
                54.0,
                57.0,
                57.0,
                56.0,
                55.0,
                57.0,
                56.0,
                55.0,
                57.0,
                54.0,
                57.0,
                54.0,
                57.0,
                57.0,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [56.0, 54.0, 53.0, 54.0, 54.0, 56.0, 56.0, 54.0],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [54.5, 56.0, 54.5, 54.5, 56.0, 54.0, 54.0, 56.5, 53.5, 54.0, 54.0, 56.5],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [55.0, 54.0, 54.0, 55.0, 54.0, 55.0, 54.0, 54.0, 55.0, 55.0, 54.0, 54.0],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [58.0, 55.0, 58.0, 56.0, 57.0, 56.0, 54.0, 56.0, 55.0],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [56.0, 56.0, 54.0, 57.0, 56.0, 53.0, 56.0, 55.0, 53.0, 56.0, 54.0, 56.0],
        ],
    ],
)
def test_load_weight(path: Path, load_weight: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.load_weight() == load_weight


@pytest.mark.parametrize(
    "path, total_time",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                108.4,
                108.8,
                108.8,
                109.2,
                109.9,
                111.0,
                111.2,
                111.2,
                112.2,
                112.3,
                112.5,
                114.6,
                116.4,
                116.5,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                85.5,
                85.6,
                86.1,
                86.3,
                86.5,
                86.6,
                86.7,
                86.9,
                87.4,
                87.4,
                88.3,
                88.5,
                88.8,
                89.8,
                90.5,
                92.3,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                122.9,
                122.9,
                122.9,
                123.1,
                123.1,
                123.2,
                123.4,
                123.7,
                124.0,
                124.0,
                124.3,
                124.7,
                124.8,
                124.9,
                125.9,
                None,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [None, None, None, None, None, None, None, None],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [92.4, 92.8, 93.3, 93.9, 94.0, 94.1, 94.1, 94.4, 94.5, 94.7, 95.1, 99.0],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [88.9, 89.1, 89.1, 89.3, 89.3, 89.5, 89.6, 89.8, 90.3, 90.7, 90.9, None],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [104.5, 106.6, 107.0, 107.2, 107.3, 107.4, 112.4, 116.4, None],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [
                114.6,
                114.9,
                115.0,
                115.1,
                115.2,
                115.2,
                115.2,
                115.2,
                115.3,
                115.9,
                117.0,
                None,
            ],
        ],
    ],
)
def test_total_time(path: Path, total_time: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.total_time() == total_time


@pytest.mark.parametrize(
    "path, final_push_time",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                40.5,
                40.7,
                40.8,
                38.8,
                40.6,
                42.3,
                42.2,
                41.7,
                43.2,
                44.2,
                43.0,
                45.5,
                47.2,
                46.0,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                36.5,
                35.9,
                37.0,
                37.1,
                37.1,
                37.4,
                37.4,
                36.3,
                37.7,
                37.4,
                37.4,
                38.2,
                38.5,
                39.9,
                39.7,
                40.5,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                36.5,
                36.4,
                36.2,
                36.9,
                36.7,
                37.0,
                37.3,
                36.7,
                37.2,
                36.2,
                38.0,
                37.7,
                37.6,
                37.4,
                39.0,
                None,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [None, None, None, None, None, None, None, None],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [40.0, 40.6, 39.6, 41.2, 39.5, 40.0, 40.2, 40.1, 42.1, 41.2, 40.6, 42.3],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [39.0, 38.8, 39.3, 39.1, 39.2, 39.5, 39.8, 39.7, 40.3, 40.3, 40.9, None],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [40.6, 40.3, 41.5, 40.7, 41.2, 43.3, 45.7, 39.5, None],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [39.2, 39.1, 38.7, 39.7, 39.6, 40.1, 39.6, 40.0, 39.6, 40.0, 41.7, None],
        ],
    ],
)
def test_final_push_time(path: Path, final_push_time: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.final_push_time() == final_push_time


@pytest.mark.parametrize(
    "path, win_odds",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                2.8,
                5.7,
                13.8,
                20.6,
                6.0,
                17.5,
                16.4,
                114.2,
                21.9,
                5.8,
                150.7,
                89.7,
                131.9,
                60.2,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                10.2,
                3.9,
                8.1,
                2.1,
                13.0,
                16.1,
                8.6,
                147.7,
                174.7,
                219.6,
                104.8,
                119.2,
                111.2,
                136.6,
                218.0,
                220.0,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                58.6,
                61.5,
                2.3,
                4.1,
                10.1,
                12.1,
                57.7,
                14.9,
                12.8,
                22.4,
                22.3,
                69.7,
                183.2,
                77.3,
                150.5,
                12.3,
            ],
        ],
        [
            script_dir / "data/race/202136123104.html",
            [None, None, None, None, None, None, None, None],
        ],
        [
            script_dir / "data/race/202142122408.html",
            [2.8, 61.1, 12.3, 2.5, 30.4, 210.6, 14.8, 14.3, 33.5, 6.2, 41.5, 159.1],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [2.2, 11.2, 24.8, 31.5, 18.0, 5.7, 113.5, 31.6, 3.2, 18.7, 61.6, None],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [3.0, 9.5, 29.2, 6.5, 2.1, 6.9, 91.9, 162.0, None],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [21.8, 2.8, 62.1, 42.8, 17.0, 5.4, 9.2, 3.2, 12.0, 312.0, 15.9, None],
        ],
    ],
)
def test_win_odds(path: Path, win_odds: list[Optional[float]]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.win_odds() == win_odds


@pytest.mark.parametrize(
    "path, prize",
    [
        [
            script_dir / "data/race/202102011201.html",
            [
                510000000,
                200000000,
                130000000,
                77000000,
                51000000,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        [
            script_dir / "data/race/202105010101.html",
            [
                510000000,
                200000000,
                130000000,
                77000000,
                51000000,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        [
            script_dir / "data/race/202106050907.html",
            [
                1098500000,
                431000000,
                275500000,
                160000000,
                106000000,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        [script_dir / "data/race/202136123104.html", [0, 0, 0, 0, 0, 0, 0, 0]],
        [
            script_dir / "data/race/202142122408.html",
            [90000000, 31500000, 18000000, 13500000, 9000000, 0, 0, 0, 0, 0, 0, 0],
        ],
        [
            script_dir / "data/race/202144123104.html",
            [280000000, 112000000, 70000000, 42000000, 28000000, 0, 0, 0, 0, 0, 0, 0],
        ],
        [
            script_dir / "data/race/202147123109.html",
            [70000000, 21000000, 10500000, 7000000, 3500000, 0, 0, 0, 0],
        ],
        [
            script_dir / "data/race/202150122910.html",
            [110000000, 44000000, 27500000, 16500000, 11000000, 0, 0, 0, 0, 0, 0, 0],
        ],
    ],
)
def test_prize(path: Path, prize: list[int]):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.prize() == prize


@pytest.mark.parametrize(
    "path, win",
    [
        (script_dir / "data/race/202102011201.html", ("7", 280)),
        (script_dir / "data/race/202105010101.html", ("2", 1020)),
        (script_dir / "data/race/202106050907.html", ("7", 5860)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", ("8", 280)),
        (script_dir / "data/race/202144123104.html", ("8", 220)),
        (script_dir / "data/race/202147123109.html", ("7", 300)),
        (script_dir / "data/race/202150122910.html", ("9", 2180)),
    ],
)
def test_payoff_win(path: Path, win):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().win() == win


@pytest.mark.parametrize(
    "path, show",
    [
        (
            script_dir / "data/race/202102011201.html",
            [("7", 140), ("8", 170), ("13", 280)],
        ),
        (
            script_dir / "data/race/202105010101.html",
            [("2", 270), ("4", 150), ("3", 220)],
        ),
        (
            script_dir / "data/race/202106050907.html",
            [("7", 1260), ("9", 1080), ("11", 150)],
        ),
        (script_dir / "data/race/202136123104.html", None),
        (
            script_dir / "data/race/202142122408.html",
            [("8", 160), ("11", 860), ("12", 230)],
        ),
        (
            script_dir / "data/race/202144123104.html",
            [("8", 130), ("2", 180), ("6", 470)],
        ),
        (
            script_dir / "data/race/202147123109.html",
            [("7", 120), ("9", 210), ("2", 330)],
        ),
        (
            script_dir / "data/race/202150122910.html",
            [("9", 470), ("6", 160), ("8", 1120)],
        ),
    ],
)
def test_payoff_show(path: Path, show):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().show() == show


@pytest.mark.parametrize(
    "path, bracket_quinella",
    [
        (script_dir / "data/race/202102011201.html", (("5", "5"), 650)),
        (script_dir / "data/race/202105010101.html", (("1", "2"), 1180)),
        (script_dir / "data/race/202106050907.html", (("4", "5"), 6770)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", (("6", "8"), 1240)),
        (script_dir / "data/race/202144123104.html", (("2", "6"), 1070)),
        (script_dir / "data/race/202147123109.html", None),
        (script_dir / "data/race/202150122910.html", (("5", "7"), 1410)),
    ],
)
def test_payoff_bracket_quinella(path: Path, bracket_quinella):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().bracket_quinella() == bracket_quinella


@pytest.mark.parametrize(
    "path, quinella",
    [
        (script_dir / "data/race/202102011201.html", (("7", "8"), 680)),
        (script_dir / "data/race/202105010101.html", (("2", "4"), 1920)),
        (script_dir / "data/race/202106050907.html", (("7", "9"), 100820)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", (("8", "11"), 7470)),
        (script_dir / "data/race/202144123104.html", (("2", "8"), 1090)),
        (script_dir / "data/race/202147123109.html", (("7", "9"), 1850)),
        (script_dir / "data/race/202150122910.html", (("6", "9"), 3090)),
    ],
)
def test_payoff_quinella(path: Path, quinella):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().quinella() == quinella


@pytest.mark.parametrize(
    "path, quinella_place",
    [
        (
            script_dir / "data/race/202102011201.html",
            [(("7", "8"), 340), (("7", "13"), 660), (("8", "13"), 930)],
        ),
        (
            script_dir / "data/race/202105010101.html",
            [(("2", "4"), 630), (("2", "3"), 980), (("3", "4"), 530)],
        ),
        (
            script_dir / "data/race/202106050907.html",
            [(("7", "9"), 20940), (("7", "11"), 2650), (("9", "11"), 2290)],
        ),
        (script_dir / "data/race/202136123104.html", None),
        (
            script_dir / "data/race/202142122408.html",
            [(("8", "11"), 2310), (("8", "12"), 540), (("11", "12"), 4070)],
        ),
        (
            script_dir / "data/race/202144123104.html",
            [(("2", "8"), 470), (("6", "8"), 840), (("2", "6"), 2110)],
        ),
        (
            script_dir / "data/race/202147123109.html",
            [(("7", "9"), 470), (("2", "7"), 750), (("2", "9"), 2460)],
        ),
        (
            script_dir / "data/race/202150122910.html",
            [(("6", "9"), 820), (("8", "9"), 4610), (("6", "8"), 3220)],
        ),
    ],
)
def test_payoff_quinella_place(path: Path, quinella_place):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().quinella_place() == quinella_place


@pytest.mark.parametrize(
    "path, exacta",
    [
        (script_dir / "data/race/202102011201.html", (("7", "8"), 1150)),
        (script_dir / "data/race/202105010101.html", (("2", "4"), 4140)),
        (script_dir / "data/race/202106050907.html", (("7", "9"), 190690)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", (("8", "11"), 9040)),
        (script_dir / "data/race/202144123104.html", (("8", "2"), 1690)),
        (script_dir / "data/race/202147123109.html", (("7", "9"), 2820)),
        (script_dir / "data/race/202150122910.html", (("9", "6"), 8940)),
    ],
)
def test_payoff_exacta(path: Path, exacta):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().exacta() == exacta


@pytest.mark.parametrize(
    "path, trio",
    [
        (script_dir / "data/race/202102011201.html", (("7", "8", "13"), 2310)),
        (script_dir / "data/race/202105010101.html", (("2", "3", "4"), 3650)),
        (script_dir / "data/race/202106050907.html", (("7", "9", "11"), 113270)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", (("8", "11", "12"), 11610)),
        (script_dir / "data/race/202144123104.html", (("2", "6", "8"), 7070)),
        (script_dir / "data/race/202147123109.html", (("2", "7", "9"), 7240)),
        (script_dir / "data/race/202150122910.html", (("6", "8", "9"), 33790)),
    ],
)
def test_payoff_trio(path: Path, trio):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().trio() == trio


@pytest.mark.parametrize(
    "path, trifecta",
    [
        (script_dir / "data/race/202102011201.html", (("7", "8", "13"), 7090)),
        (script_dir / "data/race/202105010101.html", (("2", "4", "3"), 24570)),
        (script_dir / "data/race/202106050907.html", (("7", "9", "11"), 1190440)),
        (script_dir / "data/race/202136123104.html", None),
        (script_dir / "data/race/202142122408.html", (("8", "11", "12"), 46010)),
        (script_dir / "data/race/202144123104.html", (("8", "2", "6"), 23690)),
        (script_dir / "data/race/202147123109.html", (("7", "9", "2"), 22370)),
        (script_dir / "data/race/202150122910.html", (("9", "6", "8"), 211960)),
    ],
)
def test_payoff_trifecta(path: Path, trifecta):
    race_id = path.stem
    race = Race(race_id, path.read_text())
    assert race.payoff().trifecta() == trifecta
