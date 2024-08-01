#!/usr/bin/env python3
"""
Type-annotated function element_length that takes an iterable of sequences
and returns a list of tuples
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
