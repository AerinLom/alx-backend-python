#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers using
an async comprehension over async_generator.
"""
import random
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers from
    async_generator using an async comprehension,
    then returns the list of collected numbers.
    """
    return [value async for value in async_generator()]
