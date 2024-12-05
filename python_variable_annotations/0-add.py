#!/usr/bin/env python3
"""a script for type-annotated function add that
takes a float a and a float b as arguments
and returns their sum as a float."""

def add(a: float, b: float) -> float:
    """
    Adds two float numbers and returns the result.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of the two float numbers.
    """
    return a + b
