import datetime

from scraping_netkeiba.util import date_range, parallel_map


def test_date_range():
    assert list(date_range(datetime.date(2023, 1, 1), datetime.date(2023, 1, 10))) == [
        datetime.date(2023, 1, 1),
        datetime.date(2023, 1, 2),
        datetime.date(2023, 1, 3),
        datetime.date(2023, 1, 4),
        datetime.date(2023, 1, 5),
        datetime.date(2023, 1, 6),
        datetime.date(2023, 1, 7),
        datetime.date(2023, 1, 8),
        datetime.date(2023, 1, 9),
    ]


def test_parallel_map():
    assert sorted(parallel_map(sum, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])) == [
        3,
        7,
        11,
        15,
        19,
    ]
