#!/usr/bin/env python
"""WEBパースクラステスト."""
from sas import get_response
from sas import html_parse


def test_parse_google_site():
    """GoogleのページのHTMLパース(例外がおきなければ成功とする)."""
    r = get_response.GetResponse("https://www.google.com/?hl=ja")
    r.request()
    res = r.get()
    assert(res.status_code == 200)
    s = html_parse.HtmlParse(res)
    try:
        s.parse()
    except Exception:
        assert(False)
    else:
        pass


def test_parse_steam_analytics():
    """steamのゲームデータページのパース(例外がおきなければ成功とする)."""
    r = get_response.GetResponse("https://store.steampowered.com/stats/?l=japanese")
    r.request()
    res = r.get()
    assert(res.status_code == 200)
    s = html_parse.HtmlParse(res)
    try:
        s.parse()
    except Exception:
        assert(False)
    else:
        pass


def test_parse_exception_int():
    """パース失敗例外(int変数)."""
    num = 10
    s = html_parse.HtmlParse(num)
    try:
        s.parse()
    except ValueError:
        pass
    else:
        assert(False)


def test_parse_exception_response_error():
    """パースレスポンス不正(HTTPステータスコード200以外)."""
    r = get_response.GetResponse("https://www.google.com/?hl=ja")
    r.request()
    res = r.get()
    res.status_code = 400
    assert(res.status_code == 400)
    s = html_parse.HtmlParse(res)
    try:
        s.parse()
    except ValueError:
        pass
    else:
        assert(False)
