#!/usr/bin/env python
"""HTMLパースクラス."""
from bs4 import BeautifulSoup


class HtmlParse():
    """HTMLパースクラス."""

    def __init__(self, response):
        """コンストラクタ."""
        self.__response = response
        self.__soup = None

    def parse(self):
        """HTMLのパース."""
        if self._check_response_object(self.__response) is False:
            raise ValueError("invalid response object")
        if self._check_status_ok() is False:
            raise ValueError("invalid response")
        self.__soup = BeautifulSoup(self.__response.content, "html.parser")

    def _check_response_object(self, obj) -> bool:
        """レスポンスオブジェクトのチェック."""
        return str(type(obj)) == \
            "<class 'requests.models.Response'>"

    def _check_status_ok(self) -> bool:
        """レスポンスオブジェクトからステータスコードが200OKかチェックする."""
        return self.__response.status_code == 200
