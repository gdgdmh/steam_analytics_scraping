#!/usr/bin/env python
"""steamのランキングデータクラステスト."""
from sas import ranking_data
from sas import game_data


def test_add_one():
    """データ追加(1)."""
    g = game_data.GameData("", 0, 0)
    r = ranking_data.RankingData()
    r.add(g)
    assert(r.length() == 1)


def test_add_two():
    """データ追加(2)."""
    r = ranking_data.RankingData()
    count = 2
    for _ in range(count):
        g = game_data.GameData("", 0, 0)
        r.add(g)
    assert(r.length() == count)


def test_clear_zero():
    """データのクリア(0)."""
    r = ranking_data.RankingData()
    r.clear()
    assert(r.length() == 0)


def test_clear_one():
    """データのクリア(1)."""
    r = ranking_data.RankingData()
    count = 1
    for _ in range(count):
        g = game_data.GameData("", 0, 0)
        r.add(g)
    assert(r.length() == count)


def test_clear_one_hundred():
    """データのクリア(100)."""
    r = ranking_data.RankingData()
    count = 100
    for _ in range(count):
        g = game_data.GameData("", 0, 0)
        r.add(g)
    assert(r.length() == count)


def test_length_zero():
    """データ数の取得(0)."""
    r = ranking_data.RankingData()
    assert(r.length() == 0)


def test_length_one():
    """データ数の取得(1)."""
    r = ranking_data.RankingData()
    count = 1
    for _ in range(count):
        g = game_data.GameData("", 0, 0)
        r.add(g)
    assert(r.length() == count)


def test_length_ten():
    """データ数の取得(10)."""
    r = ranking_data.RankingData()
    count = 10
    for _ in range(count):
        g = game_data.GameData("", 0, 0)
        r.add(g)
    assert(r.length() == count)


def test_get_one():
    """データの取得(1)."""
    r = ranking_data.RankingData()
    count = 1
    for _ in range(count):
        g = game_data.GameData("abc", 1, 2)
        r.add(g)
    d = r.get(0)
    assert(d.get_name() == "abc")
    assert(d.get_current_user() == 1)
    assert(d.get_max_user() == 2)


def test_get_three():
    """データの取得(3)."""
    r = ranking_data.RankingData()
    count = 3
    for i in range(count):
        if i == 0:
            g = game_data.GameData("あいう", 90, 100)
            r.add(g)
        if i == 1:
            g = game_data.GameData("漢字", 456, 513)
            r.add(g)
        if i == 2:
            g = game_data.GameData("XYZ", 1234567, 8901234)
            r.add(g)
    d = r.get(0)
    assert(d.get_name() == "あいう")
    assert(d.get_current_user() == 90)
    assert(d.get_max_user() == 100)
    d = r.get(1)
    assert(d.get_name() == "漢字")
    assert(d.get_current_user() == 456)
    assert(d.get_max_user() == 513)
    d = r.get(2)
    assert(d.get_name() == "XYZ")
    assert(d.get_current_user() == 1234567)
    assert(d.get_max_user() == 8901234)
