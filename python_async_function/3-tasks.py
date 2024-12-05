#!/usr/bin/env python3
"""Create asyncio.Task from wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay.

    Returns:
        asyncio.Task: An asyncio.Task wrapping wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
