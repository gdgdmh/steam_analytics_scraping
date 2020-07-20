#!/usr/bin/env python
"""スクレイピングクラス(steam analyticsページのアクティブ数のスクレイピング)."""
from bs4 import BeautifulSoup
from sas import ranking_data


class Scraping():
    """スクレイピングクラス."""

    def __init__(self, soup: object):
        """コンストラクタ."""
        self.__soup = soup
        self.__ranking_data = []

    def scraping(self):
        """スクレイピングの実行."""
        if self._check_beautiful_soup_object(self.__soup) is False:
            raise ValueError("invalid soup object")
        self.__ranking_data.clear()

        # 各ゲームの[現在のプレイヤー数と本日のピーク数]を取得する
        counts = self.__soup.find_all(class_="currentServers")
        # 各ゲームのタイトル名を取得する
        titles = self.__soup.find_all(class_="gameLink")

        player_count = int(len(counts))
        title_count = int(len(titles))
        # 要素数をチェック
        assert((player_count / 2) == title_count)

        for i in range(title_count):
            rd = ranking_data.RankingData(
                titles[i].text, counts[i * 2].text, counts[(i * 2) + 1].text)
            self.__ranking_data.append(rd)

    def _check_beautiful_soup_object(self, obj) -> bool:
        """BeautifulSoupオブジェクトかチェック."""
        return str(type(obj)) == \
            "<class 'bs4.BeautifulSoup'>"
