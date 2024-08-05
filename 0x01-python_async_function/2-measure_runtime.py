#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n coroutine.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time returning the average
    """
    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.time()
    runtime = finish_time - begin_time
    return runtime / n
