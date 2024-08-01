#!/usr/bin/env python3
"""
type-annotated function floor that takes a mixed list as an arg
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function that returns the sum of a mixed list
    """
    return sum(mxd_lst)
