import os.path
from pathlib import Path

import pytest

from scraping_netkeiba.horse_ped import HorsePed

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize(
    "path, sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a011c77"),
        (script_dir / "data/horse_ped/2018100498.html", "2001103312"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00fa34"),
        (script_dir / "data/horse_ped/2018100688.html", "000a01176a"),
        (script_dir / "data/horse_ped/2018100689.html", "2010105827"),
        (script_dir / "data/horse_ped/2018101424.html", "2010104298"),
        (script_dir / "data/horse_ped/2018101484.html", "000a011155"),
        (script_dir / "data/horse_ped/2018101552.html", "1995108676"),
        (script_dir / "data/horse_ped/2018101711.html", "2011103975"),
        (script_dir / "data/horse_ped/2018101965.html", "2005100097"),
        (script_dir / "data/horse_ped/2018102435.html", "2004106867"),
        (script_dir / "data/horse_ped/2018102840.html", "2009106525"),
        (script_dir / "data/horse_ped/2018103840.html", "2005105410"),
        (script_dir / "data/horse_ped/2018104480.html", "000a011c77"),
        (script_dir / "data/horse_ped/2018105460.html", "2011100655"),
        (script_dir / "data/horse_ped/2018106320.html", "2006103169"),
    ],
)
def test_horse_ped_sire(path, sire):
    assert HorsePed(path.stem, path.read_text()).sire() == sire


@pytest.mark.parametrize(
    "path, sire_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a0115e2"),
        (script_dir / "data/horse_ped/2018100498.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00010f"),
        (script_dir / "data/horse_ped/2018100688.html", "000a002133"),
        (script_dir / "data/horse_ped/2018100689.html", "2002100816"),
        (script_dir / "data/horse_ped/2018101424.html", "2001103460"),
        (script_dir / "data/horse_ped/2018101484.html", "000a000178"),
        (script_dir / "data/horse_ped/2018101552.html", "000a0019b4"),
        (script_dir / "data/horse_ped/2018101711.html", "2001103460"),
        (script_dir / "data/horse_ped/2018101965.html", "1999106689"),
        (script_dir / "data/horse_ped/2018102435.html", "000a000082"),
        (script_dir / "data/horse_ped/2018102840.html", "2002100816"),
        (script_dir / "data/horse_ped/2018103840.html", "1995108676"),
        (script_dir / "data/horse_ped/2018104480.html", "000a0115e2"),
        (script_dir / "data/horse_ped/2018105460.html", "2004103328"),
        (script_dir / "data/horse_ped/2018106320.html", "1998101786"),
    ],
)
def test_horse_ped_sire_sire(path, sire_sire):
    assert HorsePed(path.stem, path.read_text()).sire_sire() == sire_sire


@pytest.mark.parametrize(
    "path, sire_sire_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a0022d1"),
        (script_dir / "data/horse_ped/2018100498.html", "000a0012bf"),
        (script_dir / "data/horse_ped/2018100601.html", "000a000134"),
        (script_dir / "data/horse_ped/2018100688.html", "000a001d37"),
        (script_dir / "data/horse_ped/2018100689.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018101424.html", "000a001d7e"),
        (script_dir / "data/horse_ped/2018101484.html", "000a001a98"),
        (script_dir / "data/horse_ped/2018101552.html", "000a0012cb"),
        (script_dir / "data/horse_ped/2018101711.html", "000a001d7e"),
        (script_dir / "data/horse_ped/2018101965.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018102435.html", "000a0012cb"),
        (script_dir / "data/horse_ped/2018102840.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018103840.html", "000a0019b4"),
        (script_dir / "data/horse_ped/2018104480.html", "000a0022d1"),
        (script_dir / "data/horse_ped/2018105460.html", "1995108676"),
        (script_dir / "data/horse_ped/2018106320.html", "1983109006"),
    ],
)
def test_horse_ped_sire_sire_sire(path, sire_sire_sire):
    assert HorsePed(path.stem, path.read_text()).sire_sire_sire() == sire_sire_sire


@pytest.mark.parametrize(
    "path, sire_sire_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a0115f9"),
        (script_dir / "data/horse_ped/2018100498.html", "000a008c1e"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00a55c"),
        (script_dir / "data/horse_ped/2018100688.html", "000a00acaa"),
        (script_dir / "data/horse_ped/2018100689.html", "000a0003a2"),
        (script_dir / "data/horse_ped/2018101424.html", "000a00680e"),
        (script_dir / "data/horse_ped/2018101484.html", "000a00a104"),
        (script_dir / "data/horse_ped/2018101552.html", "000a008c0e"),
        (script_dir / "data/horse_ped/2018101711.html", "000a00680e"),
        (script_dir / "data/horse_ped/2018101965.html", "000a0065ef"),
        (script_dir / "data/horse_ped/2018102435.html", "000a00877c"),
        (script_dir / "data/horse_ped/2018102840.html", "000a0003a2"),
        (script_dir / "data/horse_ped/2018103840.html", "000a00a4b9"),
        (script_dir / "data/horse_ped/2018104480.html", "000a0115f9"),
        (script_dir / "data/horse_ped/2018105460.html", "1993109144"),
        (script_dir / "data/horse_ped/2018106320.html", "000a00657c"),
    ],
)
def test_horse_ped_sire_sire_dam(path, sire_sire_dam):
    print(HorsePed(path.stem, path.read_text()).sire_sire_dam())
    assert HorsePed(path.stem, path.read_text()).sire_sire_dam() == sire_sire_dam


@pytest.mark.parametrize(
    "path, sire_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a011c7c"),
        (script_dir / "data/horse_ped/2018100498.html", "000a0003a2"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00faab"),
        (script_dir / "data/horse_ped/2018100688.html", "000a011794"),
        (script_dir / "data/horse_ped/2018100689.html", "000a00646f"),
        (script_dir / "data/horse_ped/2018101424.html", "2000101560"),
        (script_dir / "data/horse_ped/2018101484.html", "000a01117d"),
        (script_dir / "data/horse_ped/2018101552.html", "000a00a4b9"),
        (script_dir / "data/horse_ped/2018101711.html", "1996107386"),
        (script_dir / "data/horse_ped/2018101965.html", "1988102419"),
        (script_dir / "data/horse_ped/2018102435.html", "000a00685a"),
        (script_dir / "data/horse_ped/2018102840.html", "1992108561"),
        (script_dir / "data/horse_ped/2018103840.html", "1994108661"),
        (script_dir / "data/horse_ped/2018104480.html", "000a011c7c"),
        (script_dir / "data/horse_ped/2018105460.html", "2001102948"),
        (script_dir / "data/horse_ped/2018106320.html", "1997103621"),
    ],
)
def test_horse_ped_sire_dam(path, sire_dam):
    assert HorsePed(path.stem, path.read_text()).sire_dam() == sire_dam


@pytest.mark.parametrize(
    "path, sire_dam_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a0017d2"),
        (script_dir / "data/horse_ped/2018100498.html", "000a001cb4"),
        (script_dir / "data/horse_ped/2018100601.html", "000a001bd6"),
        (script_dir / "data/horse_ped/2018100688.html", "000a00185f"),
        (script_dir / "data/horse_ped/2018100689.html", "000a001a98"),
        (script_dir / "data/horse_ped/2018101424.html", "1993109188"),
        (script_dir / "data/horse_ped/2018101484.html", "000a001c0e"),
        (script_dir / "data/horse_ped/2018101552.html", "000a0000d3"),
        (script_dir / "data/horse_ped/2018101711.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018101965.html", "000a000227"),
        (script_dir / "data/horse_ped/2018102435.html", "000a001607"),
        (script_dir / "data/horse_ped/2018102840.html", "1980106362"),
        (script_dir / "data/horse_ped/2018103840.html", "1983109006"),
        (script_dir / "data/horse_ped/2018104480.html", "000a0017d2"),
        (script_dir / "data/horse_ped/2018105460.html", "000a000093"),
        (script_dir / "data/horse_ped/2018106320.html", "000a000258"),
    ],
)
def test_horse_ped_sire_dam_sire(path, sire_dam_sire):
    assert HorsePed(path.stem, path.read_text()).sire_dam_sire() == sire_dam_sire


@pytest.mark.parametrize(
    "path, sire_dam_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a009bb0"),
        (script_dir / "data/horse_ped/2018100498.html", "000a00922c"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00faac"),
        (script_dir / "data/horse_ped/2018100688.html", "000a00ff8d"),
        (script_dir / "data/horse_ped/2018100689.html", "000a008ea8"),
        (script_dir / "data/horse_ped/2018101424.html", "1994108674"),
        (script_dir / "data/horse_ped/2018101484.html", "000a009e3b"),
        (script_dir / "data/horse_ped/2018101552.html", "000a00a4b8"),
        (script_dir / "data/horse_ped/2018101711.html", "000a006496"),
        (script_dir / "data/horse_ped/2018101965.html", "1980106180"),
        (script_dir / "data/horse_ped/2018102435.html", "000a00b4b2"),
        (script_dir / "data/horse_ped/2018102840.html", "000a005fff"),
        (script_dir / "data/horse_ped/2018103840.html", "1983103979"),
        (script_dir / "data/horse_ped/2018104480.html", "000a009bb0"),
        (script_dir / "data/horse_ped/2018105460.html", "1986106826"),
        (script_dir / "data/horse_ped/2018106320.html", "000a006212"),
    ],
)
def test_horse_ped_sire_dam_dam(path, sire_dam_dam):
    assert HorsePed(path.stem, path.read_text()).sire_dam_dam() == sire_dam_dam


@pytest.mark.parametrize(
    "path, dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "2011105841"),
        (script_dir / "data/horse_ped/2018100498.html", "2008105651"),
        (script_dir / "data/horse_ped/2018100601.html", "2006101198"),
        (script_dir / "data/horse_ped/2018100688.html", "2011100560"),
        (script_dir / "data/horse_ped/2018100689.html", "000a0116cd"),
        (script_dir / "data/horse_ped/2018101424.html", "2006104908"),
        (script_dir / "data/horse_ped/2018101484.html", "2003103351"),
        (script_dir / "data/horse_ped/2018101552.html", "2006106767"),
        (script_dir / "data/horse_ped/2018101711.html", "2007103017"),
        (script_dir / "data/horse_ped/2018101965.html", "2008105857"),
        (script_dir / "data/horse_ped/2018102435.html", "2013102185"),
        (script_dir / "data/horse_ped/2018102840.html", "2005104557"),
        (script_dir / "data/horse_ped/2018103840.html", "2006101034"),
        (script_dir / "data/horse_ped/2018104480.html", "2007101001"),
        (script_dir / "data/horse_ped/2018105460.html", "2005102077"),
        (script_dir / "data/horse_ped/2018106320.html", "2011103747"),
    ],
)
def test_horse_ped_sire_dam(path, dam):
    assert HorsePed(path.stem, path.read_text()).dam() == dam


@pytest.mark.parametrize(
    "path, dam_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a0103b9"),
        (script_dir / "data/horse_ped/2018100498.html", "000a00fd4c"),
        (script_dir / "data/horse_ped/2018100601.html", "1997110025"),
        (script_dir / "data/horse_ped/2018100688.html", "000a011625"),
        (script_dir / "data/horse_ped/2018100689.html", "000a001bea"),
        (script_dir / "data/horse_ped/2018101424.html", "000a00035e"),
        (script_dir / "data/horse_ped/2018101484.html", "1992109618"),
        (script_dir / "data/horse_ped/2018101552.html", "1994108729"),
        (script_dir / "data/horse_ped/2018101711.html", "1999110099"),
        (script_dir / "data/horse_ped/2018101965.html", "1996110138"),
        (script_dir / "data/horse_ped/2018102435.html", "2005110112"),
        (script_dir / "data/horse_ped/2018102840.html", "000a0000b5"),
        (script_dir / "data/horse_ped/2018103840.html", "000a0000b5"),
        (script_dir / "data/horse_ped/2018104480.html", "1995103211"),
        (script_dir / "data/horse_ped/2018105460.html", "000a00013a"),
        (script_dir / "data/horse_ped/2018106320.html", "2003102991"),
    ],
)
def test_horse_ped_dam_sire(path, dam_sire):
    assert HorsePed(path.stem, path.read_text()).dam_sire() == dam_sire


@pytest.mark.parametrize(
    "path, dam_sire_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a000178"),
        (script_dir / "data/horse_ped/2018100498.html", "000a0000d1"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00193b"),
        (script_dir / "data/horse_ped/2018100688.html", "000a0000d1"),
        (script_dir / "data/horse_ped/2018100689.html", "000a001607"),
        (script_dir / "data/horse_ped/2018101424.html", "000a001beb"),
        (script_dir / "data/horse_ped/2018101484.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018101552.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018101711.html", "000a0016f2"),
        (script_dir / "data/horse_ped/2018101965.html", "000a00010f"),
        (script_dir / "data/horse_ped/2018102435.html", "000a010545"),
        (script_dir / "data/horse_ped/2018102840.html", "000a000134"),
        (script_dir / "data/horse_ped/2018103840.html", "000a000134"),
        (script_dir / "data/horse_ped/2018104480.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018105460.html", "000a001849"),
        (script_dir / "data/horse_ped/2018106320.html", "000a00010f"),
    ],
)
def test_horse_ped_dam_sire_sire(path, dam_sire_sire):
    assert HorsePed(path.stem, path.read_text()).dam_sire_sire() == dam_sire_sire


@pytest.mark.parametrize(
    "path, dam_sire_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a01043c"),
        (script_dir / "data/horse_ped/2018100498.html", "000a00fd7f"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00abee"),
        (script_dir / "data/horse_ped/2018100688.html", "000a00fcbb"),
        (script_dir / "data/horse_ped/2018100689.html", "000a0087a5"),
        (script_dir / "data/horse_ped/2018101424.html", "000a009ac9"),
        (script_dir / "data/horse_ped/2018101484.html", "000a00021e"),
        (script_dir / "data/horse_ped/2018101552.html", "1988107344"),
        (script_dir / "data/horse_ped/2018101711.html", "000a00b2b6"),
        (script_dir / "data/horse_ped/2018101965.html", "000a0000d6"),
        (script_dir / "data/horse_ped/2018102435.html", "000a010cb3"),
        (script_dir / "data/horse_ped/2018102840.html", "000a00afb0"),
        (script_dir / "data/horse_ped/2018103840.html", "000a00afb0"),
        (script_dir / "data/horse_ped/2018104480.html", "1987101495"),
        (script_dir / "data/horse_ped/2018105460.html", "000a00a946"),
        (script_dir / "data/horse_ped/2018106320.html", "1998101750"),
    ],
)
def test_horse_ped_dam_sire_dam(path, dam_sire_dam):
    assert HorsePed(path.stem, path.read_text()).dam_sire_dam() == dam_sire_dam


@pytest.mark.parametrize(
    "path, dam_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "1999101675"),
        (script_dir / "data/horse_ped/2018100498.html", "1992107580"),
        (script_dir / "data/horse_ped/2018100601.html", "1999100606"),
        (script_dir / "data/horse_ped/2018100688.html", "2001100015"),
        (script_dir / "data/horse_ped/2018100689.html", "000a006854"),
        (script_dir / "data/horse_ped/2018101424.html", "1992110106"),
        (script_dir / "data/horse_ped/2018101484.html", "1995107768"),
        (script_dir / "data/horse_ped/2018101552.html", "1998105862"),
        (script_dir / "data/horse_ped/2018101711.html", "1993109097"),
        (script_dir / "data/horse_ped/2018101965.html", "1999102409"),
        (script_dir / "data/horse_ped/2018102435.html", "2002101029"),
        (script_dir / "data/horse_ped/2018102840.html", "000a00675d"),
        (script_dir / "data/horse_ped/2018103840.html", "000a00ff4d"),
        (script_dir / "data/horse_ped/2018104480.html", "1996105673"),
        (script_dir / "data/horse_ped/2018105460.html", "1997103396"),
        (script_dir / "data/horse_ped/2018106320.html", "2003102082"),
    ],
)
def test_horse_ped_dam_dam(path, dam_dam):
    assert HorsePed(path.stem, path.read_text()).dam_dam() == dam_dam


@pytest.mark.parametrize(
    "path, dam_dam_sire",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a000d7f"),
        (script_dir / "data/horse_ped/2018100498.html", "1984109003"),
        (script_dir / "data/horse_ped/2018100601.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018100688.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018100689.html", "000a0000cc"),
        (script_dir / "data/horse_ped/2018101424.html", "000a0000d3"),
        (script_dir / "data/horse_ped/2018101484.html", "1989109102"),
        (script_dir / "data/horse_ped/2018101552.html", "000a000d71"),
        (script_dir / "data/horse_ped/2018101711.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018101965.html", "000a0001a7"),
        (script_dir / "data/horse_ped/2018102435.html", "000a0000df"),
        (script_dir / "data/horse_ped/2018102840.html", "000a001d88"),
        (script_dir / "data/horse_ped/2018103840.html", "000a00185a"),
        (script_dir / "data/horse_ped/2018104480.html", "1983109006"),
        (script_dir / "data/horse_ped/2018105460.html", "000a00033a"),
        (script_dir / "data/horse_ped/2018106320.html", "000a000082"),
    ],
)
def test_horse_ped_dam_dam_sire(path, dam_dam_sire):
    assert HorsePed(path.stem, path.read_text()).dam_dam_sire() == dam_dam_sire


@pytest.mark.parametrize(
    "path, dam_dam_dam",
    [
        (script_dir / "data/horse_ped/2018100299.html", "000a006129"),
        (script_dir / "data/horse_ped/2018100498.html", "1988102734"),
        (script_dir / "data/horse_ped/2018100601.html", "1992110234"),
        (script_dir / "data/horse_ped/2018100688.html", "1990104543"),
        (script_dir / "data/horse_ped/2018100689.html", "000a00b4ac"),
        (script_dir / "data/horse_ped/2018101424.html", "000a009710"),
        (script_dir / "data/horse_ped/2018101484.html", "1982102104"),
        (script_dir / "data/horse_ped/2018101552.html", "1990104483"),
        (script_dir / "data/horse_ped/2018101711.html", "1988107334"),
        (script_dir / "data/horse_ped/2018101965.html", "000a006310"),
        (script_dir / "data/horse_ped/2018102435.html", "1991102100"),
        (script_dir / "data/horse_ped/2018102840.html", "000a009d01"),
        (script_dir / "data/horse_ped/2018103840.html", "000a009956"),
        (script_dir / "data/horse_ped/2018104480.html", "000a00643a"),
        (script_dir / "data/horse_ped/2018105460.html", "000a006530"),
        (script_dir / "data/horse_ped/2018106320.html", "1992110153"),
    ],
)
def test_horse_ped_dam_dam_dam(path, dam_dam_dam):
    assert HorsePed(path.stem, path.read_text()).dam_dam_dam() == dam_dam_dam
