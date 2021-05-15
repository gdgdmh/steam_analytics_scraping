#!/usr/bin/env python
"""シーンクラス."""


class Scene():
    """シーンクラス(数値で管理する)."""

    def __init__(self):
        """コンストラクタ."""
        self.__number = 0

    def set(self, num: int):
        """数値を設定."""
        self.__number = num

    def get(self) -> int:
        """数値を取得."""
        return self.__number
