#!/usr/bin/env python3
"""The basics of async"""
import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns the wait time"""
    wait_total = random.uniform(0, max_delay)
    await asyncio.sleep(wait_total)

    return wait_total
