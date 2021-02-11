#!/usr/bin/env python
"""キーボード入力テスト."""
from sas import input_keyboard


def test_input_string_mock(capsys, monkeypatch):
    """キーボード入力の取得(システムメソッドなのでダミーでテスト)."""
    method_name = 'input_string'
    p = 'aaa'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    ik = input_keyboard.InputKeyboard()
    result = ik.input_string()
    assert result == p
