#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a float and returns a multiplier function.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
