#!/usr/bin/env python3
"""
Module that defines an asynchronous coroutine waiting on a random delay.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine that waits for a random delay between 0 and max_delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
