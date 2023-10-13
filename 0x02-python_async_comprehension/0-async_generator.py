#!/usr/bin/env python3
"""
Coroutine called 'async_generator' taking no arguments.

It loops 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
random module is used.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, delay 1 sec each time
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
