#!/usr/bin/env python3
"""Measure runtime of an async function."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of wait_n and returns the average time per call.

    Args:
        n (int): Number of calls to wait_n.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: Average execution time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_runtime = end_time - start_time
    average_runtime = total_runtime / n

    return average_runtime
