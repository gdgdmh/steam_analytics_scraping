#!/usr/bin/env python
"""Webリクエストレスポンス取得クラステスト."""
from sas import get_response


def test_get_default():
    """レスポンスを取得(None)."""
    r = get_response.GetResponse("")
    assert(r.get() is None)


def test_get_google_site():
    """Googleのページのレスポンスを取得."""
    r = get_response.GetResponse("https://www.google.com/?hl=ja")
    r.request()
    res = r.get()
    assert(res.status_code == 200)


def test_request_steam_analytics():
    """steamのゲームデータページを取得できるかチェック."""
    r = get_response.GetResponse("https://store.steampowered.com/stats/?l=japanese")
    r.request()
    res = r.get()
    assert(res.status_code == 200)
