#!/usr/bin/env python3
"""A module for creating a tuple from a string and a squared number."""


from typing import List, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of the number v.

    Args:
        k (str): A string.
        v (Union[int, float]): A number.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of the number v.
    """
    return (k, float(v ** 2))
