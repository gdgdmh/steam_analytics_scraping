#!/usr/bin/env python
"""Webリクエストレスポンス取得クラス."""
import requests


class GetResponse():
    """Webリクエストレスポンス取得クラス."""

    def __init__(self, url: str):
        """コンストラクタ."""
        self.__url = url
        self.__response = None

    def get(self) -> object:
        """レスポンスオブジェクトの取得する."""
        return self.__response

    def request(self):
        """レスポンスを取得する."""
        self.__response = requests.get(self.__url)
