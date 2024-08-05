#!/usr/bin/env python3
"""
Module defining asynchronous coroutine, using delays concurrently using tasks
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with set delays
    """
    current_tasks = [task_wait_random(max_delay) for _ in range(n)]
    task_delays = await asyncio.gather(*current_tasks)
    return sorted(task_delays)
