import datetime
from concurrent.futures import ProcessPoolExecutor
from typing import Callable, Generator, Iterable, Optional, ParamSpec, TypeVar

from bs4 import BeautifulSoup, Comment
from tqdm import tqdm


def date_range(
    start: datetime.date, to: datetime.date
) -> Generator[datetime.date, None, None]:
    for d in range((to - start).days):
        yield start + datetime.timedelta(days=d)


def minify_html(html: str) -> str:
    """HTML文字列を整形する

    scriptタグ、noscriptタグ、コメントタグを削除し、整形する

    Args:
        html (str): HTML文字列

    Returns:
        str: HTML文字列
    """
    soup = BeautifulSoup(html, "html.parser")

    script_tags = soup.select("script")
    for t in script_tags:
        t.extract()

    noscript_tags = soup.select("noscript")
    for t in noscript_tags:
        t.extract()

    comment_tags = soup.find_all(string=lambda text: isinstance(text, Comment))
    for t in comment_tags:
        t.extract()

    return str(soup)


P = ParamSpec("P")
R = TypeVar("R")


def parallel_map(
    function: Callable[P, R], iterables: Iterable, desc: Optional[str] = None
) -> list[R]:
    list_from_iter = list(iterables)
    with ProcessPoolExecutor() as thread:
        return list(
            tqdm(
                thread.map(function, list_from_iter),
                total=len(list_from_iter),
                desc=desc,
            )
        )
