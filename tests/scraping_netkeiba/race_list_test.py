import datetime
import os.path
from pathlib import Path

import pytest

from scraping_netkeiba.client import RaceSumParam
from scraping_netkeiba.race_list import RaceList

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = script_dir / "data/race_list"


def test_init_invalid():
    html = (data_dir / "20100101.html").read_text()
    with pytest.raises(Exception) as _:
        RaceList(datetime.date(2010, 10, 1), html)


def test_race_date():
    # Prepare
    html = (data_dir / "20100101.html").read_text()
    race_list = RaceList(datetime.date(2010, 1, 5), html)
    # Run
    actual: datetime.date = race_list.race_date()
    expected: datetime.date = datetime.date(2010, 1, 5)
    # Assert
    assert actual == expected


def test_race_sum_params():
    # Prepare
    html = (data_dir / "20100101.html").read_text()
    race_list = RaceList(datetime.date(2010, 1, 5), html)
    # Run
    actual = race_list.race_sum_params()
    expected = [
        RaceSumParam("06", datetime.date(2010, 1, 5)),
        RaceSumParam("08", datetime.date(2010, 1, 5)),
        RaceSumParam("65", datetime.date(2010, 1, 5)),
    ]
    # Assert
    assert actual == expected
