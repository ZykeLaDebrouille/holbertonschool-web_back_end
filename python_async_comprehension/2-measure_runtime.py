#!/usr/bin/env python3
"""
Module 2-measure_runtime
Ce module contient une coroutine qui mesure le temps total
pour exécuter 4 appels de async_comprehension en parallèle.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps total pour exécuter 4 appels de async_comprehension en parallèle.

    Retourne :
        Le temps total d'exécution (float, en secondes).
    """
    start = time.time()

    # Exécuter 4 appels de async_comprehension en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()
    return end - start
