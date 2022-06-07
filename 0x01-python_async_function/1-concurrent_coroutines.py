#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list showing called wait_random n times"""
    results = []
    delays = [wait_random(max_delay) for time in range(n)]

    for sort in asyncio.as_completed(delays):
        val = await sort
        results.append(val)

    return results
