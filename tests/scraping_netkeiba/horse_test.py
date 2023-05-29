import datetime
import os.path
from pathlib import Path

import pytest

from scraping_netkeiba.horse import Horse

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize(
    "path, error_message",
    [
        [
            script_dir / "data/horse/invalid_empty.html",
            "Active horse url is not found",
        ],
        [
            script_dir / "data/horse/invalid_active_horse_url_is_not_found.html",
            "Active horse url is not found",
        ],
        [
            script_dir / "data/horse/invalid_horse_id.html",
            'Invalid horse id: expected "invalid_horse_id", got "2018106320"',
        ],
    ],
)
def test_horse_init(path: Path, error_message: str):
    with pytest.raises(Exception) as e:
        Horse(path.stem, path.read_text())
    assert str(e.value) == error_message


@pytest.mark.parametrize(
    "path, name",
    [
        [script_dir / "data/horse/2018100299.html", "フクノルッカ"],
        [script_dir / "data/horse/2018100498.html", "モッツアフィアート"],
        [script_dir / "data/horse/2018100601.html", "シンシアハート"],
        [script_dir / "data/horse/2018100688.html", "アウリッシュ"],
        [script_dir / "data/horse/2018100689.html", "グリーンシュート"],
        [script_dir / "data/horse/2018101424.html", "キタノコンキスタ"],
        [script_dir / "data/horse/2018101484.html", "ファインヒューズ"],
        [script_dir / "data/horse/2018101552.html", "キボウノヒビキ"],
        [script_dir / "data/horse/2018101711.html", "ナンノコレシキ"],
        [script_dir / "data/horse/2018101965.html", "ドナリノ"],
        [script_dir / "data/horse/2018102435.html", "ベストシーズン"],
        [script_dir / "data/horse/2018102840.html", "ボンバーガール"],
        [script_dir / "data/horse/2018103840.html", "タミルナードゥ"],
        [script_dir / "data/horse/2018104480.html", "ホープケツァール"],
        [script_dir / "data/horse/2018105460.html", "プレフェリータ"],
        [script_dir / "data/horse/2018106320.html", "ナイアレ"],
    ],
)
def test_horse_name(path: Path, name):
    assert Horse(path.stem, path.read_text()).name() == name


@pytest.mark.parametrize(
    "path, eng_name",
    [
        [script_dir / "data/horse/2018100299.html", "Fukuno Lukka"],
        [script_dir / "data/horse/2018100498.html", "Mozzafiato"],
        [script_dir / "data/horse/2018100601.html", "Sincere Heart"],
        [script_dir / "data/horse/2018100688.html", "Owlish"],
        [script_dir / "data/horse/2018100689.html", "Green Shoot"],
        [script_dir / "data/horse/2018101424.html", "Kitano Conquista"],
        [script_dir / "data/horse/2018101484.html", "Fine Hughes"],
        [script_dir / "data/horse/2018101552.html", "Kibono Hibiki"],
        [script_dir / "data/horse/2018101711.html", "Nannokoreshiki"],
        [script_dir / "data/horse/2018101965.html", "Dona Lino"],
        [script_dir / "data/horse/2018102435.html", "Best Season"],
        [script_dir / "data/horse/2018102840.html", "Bomber Girl"],
        [script_dir / "data/horse/2018103840.html", "Tamil Nadu"],
        [script_dir / "data/horse/2018104480.html", "Hope Quetzal"],
        [script_dir / "data/horse/2018105460.html", "Preferita"],
        [script_dir / "data/horse/2018106320.html", "Nai Are"],
    ],
)
def test_horse_eng_name(path: Path, eng_name):
    assert Horse(path.stem, path.read_text()).eng_name() == eng_name


@pytest.mark.parametrize(
    "path, gender",
    [
        [script_dir / "data/horse/2018100299.html", "牝"],
        [script_dir / "data/horse/2018100498.html", "牝"],
        [script_dir / "data/horse/2018100601.html", "牝"],
        [script_dir / "data/horse/2018100688.html", "牝"],
        [script_dir / "data/horse/2018100689.html", "牝"],
        [script_dir / "data/horse/2018101424.html", "牝"],
        [script_dir / "data/horse/2018101484.html", "牝"],
        [script_dir / "data/horse/2018101552.html", "牝"],
        [script_dir / "data/horse/2018101711.html", "牝"],
        [script_dir / "data/horse/2018101965.html", "牝"],
        [script_dir / "data/horse/2018102435.html", "牝"],
        [script_dir / "data/horse/2018102840.html", "牝"],
        [script_dir / "data/horse/2018103840.html", "牝"],
        [script_dir / "data/horse/2018104480.html", "牝"],
        [script_dir / "data/horse/2018105460.html", "牝"],
        [script_dir / "data/horse/2018106320.html", "牝"],
    ],
)
def test_horse_gender(path: Path, gender):
    assert Horse(path.stem, path.read_text()).gender() == gender


@pytest.mark.parametrize(
    "path, birth_date",
    [
        [script_dir / "data/horse/2018100299.html", datetime.date(2018, 3, 20)],
        [script_dir / "data/horse/2018100498.html", datetime.date(2018, 4, 18)],
        [script_dir / "data/horse/2018100601.html", datetime.date(2018, 5, 12)],
        [script_dir / "data/horse/2018100688.html", datetime.date(2018, 3, 7)],
        [script_dir / "data/horse/2018100689.html", datetime.date(2018, 4, 5)],
        [script_dir / "data/horse/2018101424.html", datetime.date(2018, 3, 8)],
        [script_dir / "data/horse/2018101484.html", datetime.date(2018, 5, 15)],
        [script_dir / "data/horse/2018101552.html", datetime.date(2018, 3, 31)],
        [script_dir / "data/horse/2018101711.html", datetime.date(2018, 4, 26)],
        [script_dir / "data/horse/2018101965.html", datetime.date(2018, 2, 26)],
        [script_dir / "data/horse/2018102435.html", datetime.date(2018, 4, 29)],
        [script_dir / "data/horse/2018102840.html", datetime.date(2018, 3, 5)],
        [script_dir / "data/horse/2018103840.html", datetime.date(2018, 4, 2)],
        [script_dir / "data/horse/2018104480.html", datetime.date(2018, 1, 20)],
        [script_dir / "data/horse/2018105460.html", datetime.date(2018, 3, 2)],
        [script_dir / "data/horse/2018106320.html", datetime.date(2018, 5, 12)],
    ],
)
def test_horse_gender(path: Path, birth_date):
    assert Horse(path.stem, path.read_text()).birth_date() == birth_date


@pytest.mark.parametrize(
    "path, trainer_id",
    [
        [script_dir / "data/horse/2018100299.html", "a02be"],
        [script_dir / "data/horse/2018100498.html", "05726"],
        [script_dir / "data/horse/2018100601.html", "a0043"],
        [script_dir / "data/horse/2018100688.html", "01023"],
        [script_dir / "data/horse/2018100689.html", "00359"],
        [script_dir / "data/horse/2018101424.html", "01076"],
        [script_dir / "data/horse/2018101484.html", "05726"],
        [script_dir / "data/horse/2018101552.html", "01063"],
        [script_dir / "data/horse/2018101711.html", "05275"],
        [script_dir / "data/horse/2018101965.html", "01088"],
        [script_dir / "data/horse/2018102435.html", "05333"],
        [script_dir / "data/horse/2018102840.html", "05741"],
        [script_dir / "data/horse/2018103840.html", "05200"],
        [script_dir / "data/horse/2018104480.html", "05590"],
        [script_dir / "data/horse/2018105460.html", "01017"],
        [script_dir / "data/horse/2018106320.html", "a02a3"],
    ],
)
def test_horse_trainer_id(path: Path, trainer_id):
    assert Horse(path.stem, path.read_text()).trainer_id() == trainer_id


@pytest.mark.parametrize(
    "path, owner_id",
    [
        [script_dir / "data/horse/2018100299.html", "159033"],
        [script_dir / "data/horse/2018100498.html", "333803"],
        [script_dir / "data/horse/2018100601.html", "x0a6fc"],
        [script_dir / "data/horse/2018100688.html", "003060"],
        [script_dir / "data/horse/2018100689.html", "003060"],
        [script_dir / "data/horse/2018101424.html", "163002"],
        [script_dir / "data/horse/2018101484.html", "x0acaf"],
        [script_dir / "data/horse/2018101552.html", "871006"],
        [script_dir / "data/horse/2018101711.html", "443030"],
        [script_dir / "data/horse/2018101965.html", "440006"],
        [script_dir / "data/horse/2018102435.html", "x0aa1e"],
        [script_dir / "data/horse/2018102840.html", "x0982f"],
        [script_dir / "data/horse/2018103840.html", "x03adc"],
        [script_dir / "data/horse/2018104480.html", "947031"],
        [script_dir / "data/horse/2018105460.html", "808800"],
        [script_dir / "data/horse/2018106320.html", "a00028"],
    ],
)
def test_horse_owner_id(path: Path, owner_id):
    assert Horse(path.stem, path.read_text()).owner_id() == owner_id


@pytest.mark.parametrize(
    "path, breeder_id",
    [
        [script_dir / "data/horse/2018100299.html", "670543"],
        [script_dir / "data/horse/2018100498.html", "033357"],
        [script_dir / "data/horse/2018100601.html", "503393"],
        [script_dir / "data/horse/2018100688.html", "811540"],
        [script_dir / "data/horse/2018100689.html", "811540"],
        [script_dir / "data/horse/2018101424.html", "600330"],
        [script_dir / "data/horse/2018101484.html", "530331"],
        [script_dir / "data/horse/2018101552.html", "930498"],
        [script_dir / "data/horse/2018101711.html", "210543"],
        [script_dir / "data/horse/2018101965.html", "790540"],
        [script_dir / "data/horse/2018102435.html", "713058"],
        [script_dir / "data/horse/2018102840.html", "710470"],
        [script_dir / "data/horse/2018103840.html", "833077"],
        [script_dir / "data/horse/2018104480.html", "801307"],
        [script_dir / "data/horse/2018105460.html", "301513"],
        [script_dir / "data/horse/2018106320.html", "000014"],
    ],
)
def test_horse_owner_id(path: Path, breeder_id):
    assert Horse(path.stem, path.read_text()).breeder_id() == breeder_id
