#!/usr/bin/env python
"""スクレイピングメインクラス."""
from sas import get_response
from sas import html_parse
from sas import scraping


class SasMain():
    """スクレイピングメインクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__res = None
        self.__soup = None
        self.__scraping = None

    def task(self):
        """メイン処理."""
        self._get_response()
        self._parse()
        self._scraping()
        self._find_name("Cou")

    def task2(self):
        """メイン処理."""
        self._routine()

    def _get_response(self):
        """HTMLデータをリクエストして取得する."""
        url = "https://store.steampowered.com/stats/?l=japanese"
        self.__res = get_response.GetResponse(url)
        self.__res.request()

    def _parse(self):
        """HTMLパースを行う."""
        res = self.__res.get()
        s = html_parse.HtmlParse(res)
        s.parse()
        self.__soup = s.get()

    def _scraping(self):
        """スクレイピング実行."""
        self.__scraping = scraping.Scraping(self.__soup)
        self.__scraping.scraping()

    def _find_name(self, name: str):
        """スクレイピング結果から名前の検索."""
        d = self.__scraping.find_name(name)
        if d:
            print("game title    " + d.get_name())
            print("current user  " + d.get_current_user())
            print("max user      " + d.get_max_user())

    def _print_example_command(self):
        """コマンド例を出力."""
        print("コマンドを入力して下さい")
        print("終了:exit ")

    def _routine(self):
        """ルーチン処理."""
        # データ取得、スクレイピング
        self._routine_get_data()
        self._routine_parse()
        self._routine_scraping()
        # ユーザーに聞く処理
        self._routine_ask()
        pass

    def _routine_get_data(self):
        """データ取得処理."""
        self._get_response()

    def _routine_parse(self):
        """パース処理."""
        self._parse()

    def _routine_scraping(self):
        """スクレイピング."""
        self._scraping()

    def _routine_ask(self):
        """ユーザーに聞く処理."""
        pass
