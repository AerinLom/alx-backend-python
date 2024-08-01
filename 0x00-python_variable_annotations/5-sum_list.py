#!/usr/bin/env python3
"""
type-annotated function floor that takes a list as an arg
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a type-annotated function that returns the sum of a list
    """
    return sum(input_list)
