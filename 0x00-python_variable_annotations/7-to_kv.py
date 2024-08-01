#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes a string and a number as arguments.
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number as a float.
    """
    return (k, (v * v))
