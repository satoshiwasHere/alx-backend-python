'''
Import async_comprehension (previous file) & write a measure_runtime coroutine
that will execute async_comprehension 4 times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
'''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    return end_time - start_time
