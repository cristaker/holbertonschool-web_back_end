#!/usr/bin/env python3
'''
1. Let's execute multiple coroutines at the same time with async
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine called wait_n that takes in 2 int arguments: max_delay and n.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    '''
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    # Create queue with results depending on the function have the result ready
    # Read more: shorturl.at/grAUY
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
