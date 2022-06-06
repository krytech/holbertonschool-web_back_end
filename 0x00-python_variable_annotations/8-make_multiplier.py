#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns  function that multiples a float by a multiplier"""
    def multi_func(number: float) -> float:
        return number * multiplier
    return multi_func
