#!/usr/bin/env python
"""キーボード文字入力クラス."""
from sas import input_string


class InputKeyboard(input_string.InputString):
    """キーボード文字入力クラス."""

    def input_string(self) -> str:
        """文字入力."""
        return input()
