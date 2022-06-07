#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list showing called wait_random n times"""
    results = []
    delays = [task_wait_random(max_delay) for time in range(n)]

    for sort in asyncio.as_completed(delays):
        val = await sort
        results.append(val)

    return results
