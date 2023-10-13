#!/usr/bin/env python3
'''
From the previous file, import wait_n into 2-measure_runtime.py.
Desc: Create a measure_time function with integers n and
    max_delay as arguments that evaluate the total execution
    time for wait_n(n, max_delay), and returns total_time / n.
    Your function should return a float.
Arg: n: int, max_delay: int
'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    evaluates the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
