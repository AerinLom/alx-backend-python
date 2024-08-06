#!/usr/bin/env python3
"""
Coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.
    """
    exec_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    runtime = time.time() - exec_time
    return runtime
