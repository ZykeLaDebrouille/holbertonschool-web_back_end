#!/usr/bin/env python3
"""
Module 1-async_comprehension
Ce module contient une coroutine qui collecte 10 nombres aléatoires
générés par async_generator et retourne une liste de ces nombres.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine asynchrone qui collecte 10 nombres aléatoires générés
    par async_generator, puis retourne la liste de ces nombres.

    Retourne :
        Une liste contenant 10 nombres aléatoires (float).
    """
    return [value async for value in async_generator()]
