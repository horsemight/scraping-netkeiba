import datetime

import pytest

from scraping_netkeiba.url import (
    Race,
    breeder,
    horse,
    horse_ped,
    horse_result,
    owner,
    race_list,
    race_sum,
    trainer,
)


def test_race():
    assert (
        Race("202136123101").generate() == "https://db.netkeiba.com/race/202136123101/"
    )


def test_race_invalid():
    with pytest.raises(ValueError) as e:
        Race("0" * 11)
        Race("0" * 13)
        Race("2021/1010101")
        Race("2021-1010101")
        Race("2021_1010101")


def test_race_list():
    assert (
        race_list(datetime.date(2022, 1, 10))
        == "https://db.netkeiba.com/race/list/20220110/"
    )


def test_race_sum():
    assert (
        race_sum("06", datetime.date(2022, 9, 17))
        == "https://db.netkeiba.com/race/sum/06/20220917/"
    )


def test_horse():
    assert horse("2018105460") == "https://db.netkeiba.com/horse/2018105460/"


def test_horse_invalid_horse_id_length():
    with pytest.raises(ValueError) as e:
        horse("0" * 9)
        horse("0" * 11)


def test_horse_invalid_horse_id_chars():
    with pytest.raises(ValueError) as e:
        horse("2021/10101")
        horse("2021-10101")
        horse("2021_10101")


def test_horse_result():
    assert (
        horse_result("2018105460") == "https://db.netkeiba.com/horse/result/2018105460/"
    )


def test_horse_result_invalid_horse_id_length():
    with pytest.raises(ValueError) as e:
        horse_result("0" * 9)
        horse_result("0" * 11)


def test_horse_result_invalid_horse_id_chars():
    with pytest.raises(ValueError) as e:
        horse_result("2021/10101")
        horse_result("2021-10101")
        horse_result("2021_10101")


def test_horse_ped():
    assert horse_ped("2018105460") == "https://db.netkeiba.com/horse/ped/2018105460/"


def test_horse_ped_invalid_horse_id_length():
    with pytest.raises(ValueError) as e:
        horse_ped("0" * 9)
        horse_ped("0" * 11)


def test_horse_ped_invalid_horse_id_chars():
    with pytest.raises(ValueError) as e:
        horse_ped("2021/10101")
        horse_ped("2021-10101")
        horse_ped("2021_10101")


def test_breeder():
    assert breeder("123456") == "https://db.netkeiba.com/breeder/123456/"


def test_breeder_invalid_breeder_id_length():
    with pytest.raises(ValueError) as e:
        breeder("0" * 5)
        breeder("0" * 7)


def test_breeder_invalid_breeder_id_chars():
    with pytest.raises(ValueError) as e:
        breeder("1/3456")
        breeder("1-3456")
        breeder("1_3456")


def test_owner():
    assert owner("a23456") == "https://db.netkeiba.com/owner/a23456/"


def test_owner_invalid_owner_id_length():
    with pytest.raises(ValueError) as e:
        owner("0" * 5)
        owner("0" * 7)


def test_owner_invalid_owner_id_chars():
    with pytest.raises(ValueError) as e:
        owner("a/3456")
        owner("a-3456")
        owner("a_3456")


def test_trainer():
    assert trainer("12345") == "https://db.netkeiba.com/trainer/12345/"


def test_trainer_invalid_trainer_id_length():
    with pytest.raises(ValueError) as e:
        trainer("0" * 4)
        trainer("0" * 6)


def test_trainer_invalid_trainer_id_chars():
    with pytest.raises(ValueError) as e:
        trainer("1/345")
        trainer("1-345")
        trainer("1_345")
