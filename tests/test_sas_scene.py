#!/usr/bin/env python
"""シーンクラステスト."""
from sas import sas_scene


def test_init_scene_zero():
    """初期化後のシーンが0になっているか."""
    s = sas_scene.Scene()
    assert(s.get() == 0)


def test_set_two():
    """setで2を設定."""
    s = sas_scene.Scene()
    s.set(2)
    assert(s.get() == 2)


def test_set_ten():
    """setで10を設定."""
    s = sas_scene.Scene()
    s.set(10)
    assert(s.get() == 10)


def test_set_one_hundred_twenty():
    """setで120を設定."""
    s = sas_scene.Scene()
    s.set(120)
    assert(s.get() == 120)


def test_set_five_hundred():
    """setで500を設定."""
    s = sas_scene.Scene()
    s.set(500)
    assert(s.get() == 500)


def test_get_six():
    """getで6を取得."""
    s = sas_scene.Scene()
    s.set(6)
    assert(s.get() == 6)


def test_get_nineteen():
    """getで19を取得."""
    s = sas_scene.Scene()
    s.set(19)
    assert(s.get() == 19)


def test_get_seven_hundred_three():
    """getで703を取得."""
    s = sas_scene.Scene()
    s.set(703)
    assert(s.get() == 703)
