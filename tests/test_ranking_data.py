#!/usr/bin/env python
"""steamのランキングデータクラステスト."""
from sas import ranking_data


def test_get_name_alphabet():
    """アルファベットの名前の取得."""
    n = "abc"
    rd = ranking_data.RankingData(n, 0, 0)
    assert(rd.get_name() == n)


def test_get_name_hiragana():
    """平仮名の名前の取得."""
    n = "あいうえおわをん"
    rd = ranking_data.RankingData(n, 0, 0)
    assert(rd.get_name() == n)


def test_get_name_kanji():
    """漢字の名前の取得."""
    n = "怒首領蜂"
    rd = ranking_data.RankingData(n, 0, 0)
    assert(rd.get_name() == n)


def test_get_name_special_character():
    """特殊記号の名前の取得."""
    n = "™"
    rd = ranking_data.RankingData(n, 0, 0)
    assert(rd.get_name() == n)


def test_get_current_user_zero():
    """現在のユーザー数の取得(0)."""
    c = 0
    rd = ranking_data.RankingData("a", c, 0)
    assert(rd.get_current_user() == c)


def test_get_current_user_thousand():
    """現在のユーザー数の取得(1000)."""
    c = 1000
    rd = ranking_data.RankingData("a", c, 0)
    assert(rd.get_current_user() == c)


def test_get_current_user_million():
    """現在のユーザー数の取得(1000000)."""
    c = 1000000
    rd = ranking_data.RankingData("a", c, 0)
    assert(rd.get_current_user() == c)


def test_get_max_user_zero():
    """最大ユーザー数の取得(0)."""
    m = 0
    rd = ranking_data.RankingData("a", 0, m)
    assert(rd.get_max_user() == m)


def test_get_max_user_thousand():
    """最大ユーザー数の取得(1000)."""
    m = 1000
    rd = ranking_data.RankingData("a", 0, m)
    assert(rd.get_max_user() == m)


def test_get_max_user_million():
    """最大ユーザー数の取得(1000000)."""
    m = 1000000
    rd = ranking_data.RankingData("a", 0, m)
    assert(rd.get_max_user() == m)


def test_all_parameter_ansi_zero_zero():
    """全てのパラメータをテスト(ANSI文字, 0, 0)."""
    n = "apple"
    c = 0
    m = 0
    rd = ranking_data.RankingData(n, c, m)
    assert(rd.get_name() == n)
    assert(rd.get_current_user() == c)
    assert(rd.get_max_user() == m)


def test_all_parameter_hiragana_2thousand_3million():
    """全てのパラメータをテスト(平仮名, 2000, 3000000)."""
    n = "あかさたなはまやらわ"
    c = 2000
    m = 3000000
    rd = ranking_data.RankingData(n, c, m)
    assert(rd.get_name() == n)
    assert(rd.get_current_user() == c)
    assert(rd.get_max_user() == m)
