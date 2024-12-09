#!/usr/bin/env python3


import asyncio
from random import uniform

async def async_generator():
    """
    Coroutine asynchrone qui génère 10 nombres aléatoires
    entre 0 et 10, avec une pause d'une seconde entre chaque.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Pause d'une seconde
        yield uniform(0, 10)  # Génère un nombre aléatoire
