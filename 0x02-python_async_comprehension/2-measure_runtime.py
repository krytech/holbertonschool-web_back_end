#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4x in parallel using asyncio.gather"""
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()

    return end_time - start_time
