#!/usr/bin/env python
"""文字入力インターフェース."""
from abc import ABCMeta, abstractmethod


class InputString(metaclass=ABCMeta):
    """文字入力インターフェース."""

    @abstractmethod
    def input_string(self) -> str:
        """文字入力."""
        return ""
