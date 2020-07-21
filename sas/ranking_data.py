#!/usr/bin/env python
"""steamのランキングデータクラス."""


class RankingData():
    """steamのランキングデータクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__list = []

    def add(self, game_data: object):
        """ランキングデータの追加."""
        self.__list.append(game_data)

    def clear(self):
        """ランキングデータのクリア."""
        self.__list.clear()

    def length(self) -> int:
        """ランキングデータ数を取得."""
        return len(self.__list)

    def get(self, index) -> object:
        """ランキングデータの取得."""
        return self.__list[index]

    def print(self):
        """出力."""
        for g in self.__list:
            g.print()
