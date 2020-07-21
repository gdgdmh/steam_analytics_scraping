#!/usr/bin/env python
"""steamのゲームデータクラス(ゲームタイトル, 本日の現在のユーザー数, 本日の最大ユーザー数)."""


class GameData():
    """steamのゲームデータクラス."""

    def __init__(self, name: str,
                 current_user: int, max_user: int):
        """コンストラクタ."""
        self.__name = name
        self.__current_user = current_user
        self.__max_user = max_user

    def get_name(self) -> str:
        """名前の取得."""
        return self.__name

    def get_current_user(self) -> int:
        """現在のユーザー数の取得."""
        return self.__current_user

    def get_max_user(self) -> int:
        """最大ユーザー数の取得."""
        return self.__max_user

    def print(self):
        """出力."""
        print("[" + self.__name + "," +
              str(self.__current_user) + "," + str(self.__max_user) + "]")
