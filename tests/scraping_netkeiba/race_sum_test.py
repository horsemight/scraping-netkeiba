import os
from pathlib import Path
from typing import List, NamedTuple

import pytest

from scraping_netkeiba.client import RaceParam
from scraping_netkeiba.race_sum import RaceSum

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
data_dir = script_dir / "data/race_sum"


class RaceSumRaceParamsCase(NamedTuple):
    html: str
    race_params: List[RaceParam]


def race_sum_race_params_cases():
    return [
        RaceSumRaceParamsCase(
            (data_dir / "20100814.html").read_text(),
            [
                RaceParam(race_id="201001010101"),
                RaceParam(race_id="201001010102"),
                RaceParam(race_id="201001010103"),
                RaceParam(race_id="201001010104"),
                RaceParam(race_id="201001010105"),
                RaceParam(race_id="201001010106"),
                RaceParam(race_id="201001010107"),
                RaceParam(race_id="201001010108"),
                RaceParam(race_id="201001010109"),
                RaceParam(race_id="201001010110"),
                RaceParam(race_id="201001010111"),
                RaceParam(race_id="201001010112"),
            ],
        ),
        RaceSumRaceParamsCase(
            (data_dir / "20221221.html").read_text(),
            [
                RaceParam(race_id="202243122101"),
                RaceParam(race_id="202243122102"),
                RaceParam(race_id="202243122103"),
                RaceParam(race_id="202243122104"),
                RaceParam(race_id="202243122105"),
                RaceParam(race_id="202243122106"),
                RaceParam(race_id="202243122107"),
                RaceParam(race_id="202243122108"),
                RaceParam(race_id="202243122109"),
                RaceParam(race_id="202243122110"),
                RaceParam(race_id="202243122111"),
                RaceParam(race_id="202243122112"),
            ],
        ),
    ]


@pytest.mark.parametrize("case", race_sum_race_params_cases())
def test_race_sum_race_params(case: RaceSumRaceParamsCase):
    # Prepare
    race_sum = RaceSum(case.html)
    # Run
    race_params = race_sum.race_params()
    # Assert
    assert race_params == case.race_params
