#!/usr/bin/env python3
"""
Module 0-async_generator
Ce module contient une coroutine qui génère 10 nombres aléatoires entre 0 et 10.
"""

import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine asynchrone qui génère 10 nombres aléatoires
    entre 0 et 10, avec une pause d'une seconde entre chaque.

    Retourne :
        Un générateur asynchrone de nombres aléatoires (float).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
