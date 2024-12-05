#!/usr/bin/env python3
""" async routine called wait_n that takes in 2 int arguments"""

import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with max_delay and return
        the list of all the delays"""
    tasks = [asyncio.create_task(wait_n(max_delay)) for _ in range(n)]
    delays = []

    # Insert the results into the sorted delays list
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        # Insert the delay into the sorted delays list
        for index, current_delay in enumerate(delays):
            if delay < current_delay:
                delays.insert(index, delay)
                break
        else:
            delays.append(delay)

    return delays
