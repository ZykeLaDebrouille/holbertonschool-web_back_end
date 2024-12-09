async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine asynchrone qui collecte 10 nombres aléatoires générés
    par async_generator, puis retourne la liste de ces nombres.
    """
    return [value_generated async for value_generated in async_generator()]
