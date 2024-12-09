#!/usr/bin/env python3


async_comprehension = __import__('1-async_comprehension').async_comprehension
import time, asyncio

async def measure_runtime():
    """
    Mesure le temps total pour exécuter 4 appels de async_comprehension en parallèle.
    """
    start = time.time()  # Début de la mesure

    # exécute 4 appels de async_comprehension en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()  # Fin de la mesure
    return end - start  # Retourne le temps total (fin - début)
