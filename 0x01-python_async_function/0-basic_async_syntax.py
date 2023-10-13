#!/usr/bin/env python3
'''
Desc: asynchronous coroutine taking in an integer argument,
(max_delay, with a default value of 10) named wait_random,
that waits for a random delay between 0 and max_delay,
(included and float value) seconds and eventually returns it,
Arg: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Wait up a random no of seconds, then return length of delay
    '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
