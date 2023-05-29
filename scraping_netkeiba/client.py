import abc
import datetime
import time
from pathlib import Path
from typing import NamedTuple, Optional
from urllib.parse import urlparse

import requests

from scraping_netkeiba import url


class ICache(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def exists(self, url: str) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def write(self, url: str, html: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def read(self, url: str) -> str:
        raise NotImplementedError()


class NullCache(ICache):
    def exists(self, url: str) -> bool:
        pass

    def write(self, url: str, html: str) -> None:
        pass

    def read(self, url: str) -> str:
        pass


class Cache(ICache):
    def __init__(self, cache_dir: str):
        self.__cache_dir = cache_dir

    def __cache_path(self, url: str):
        return Path(self.__cache_dir) / Path(urlparse(url).path.strip("/") + ".html")

    def exists(self, url: str) -> bool:
        return self.__cache_path(url).exists()

    def write(self, url: str, html: str) -> None:
        path = self.__cache_path(url)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html)

    def read(self, url: str) -> str:
        return self.__cache_path(url).read_text()


class HorseParam(NamedTuple):
    horse_id: str


class HorsePedParam(NamedTuple):
    horse_id: str


class RaceParam(NamedTuple):
    race_id: str


class RaceListParam(NamedTuple):
    date: datetime.date


class RaceSumParam(NamedTuple):
    track_id: str
    date: datetime.date


class Client:
    """
    netkeiba.comのHTMLを取得するクライアント
    """

    def __init__(self, cache: Optional[ICache] = None):
        self.__cache = cache or NullCache()

    def get_by_path(self, path: str, update_cache: bool = False) -> str:
        """指定されたURLパスのHTMLを取得する

        Args:
            path (str): netkeiba.comのURLパス
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.parse(path), update_cache)

    def horse(self, param: HorseParam, update_cache: bool = False) -> str:
        """競走馬のTOPページのHTMLを取得する

        Args:
            param (HorseParam): パラメータ
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.horse(param.horse_id), update_cache)

    def horse_ped(self, param: HorsePedParam, update_cache: bool = False) -> str:
        """競走馬の血統ページのHTMLを取得する

        Args:
            param (str): パラメータ
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.horse_ped(param.horse_id), update_cache)

    def race(self, param: RaceParam, update_cache: bool = False) -> str:
        """レース結果ページのHTMLを取得する

        Args:
            param (RaceParam): パラメータ
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.race(param.race_id), update_cache)

    def race_list(self, param: RaceListParam, update_cache: bool = False) -> str:
        """日別のレース一覧ページのHTMLを取得する

        Args:
            param (RaceListParam): パラメータ
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.race_list(param.date), update_cache)

    def race_sum(self, param: RaceSumParam, update_cache: bool = False) -> str:
        """競馬場・日別のレース一覧ページのHTMLを取得する

        Args:
            param (RaceSumParam): パラメータ
            update_cache (bool): キャッシュを更新するか

        Returns:
            str: HTML文字列
        """
        return self.__get(url.race_sum(param.track_id, param.date), update_cache)

    def __get(self, url: str, update_cache: bool = False) -> str:
        if not update_cache and self.__cache.exists(url):
            return self.__cache.read(url)
        response = requests.get(url)
        time.sleep(0.2)
        response.encoding = "EUC-JP"
        html = response.text
        self.__cache.write(url, html)
        return html
