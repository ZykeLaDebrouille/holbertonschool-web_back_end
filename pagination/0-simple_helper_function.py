#!/usr/bin/env python3
"""
Module for calculating index range for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a page of data.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    # Calcul de l'index de début
    start = (page - 1) * page_size
    # Calcul de l'index de fin
    end = page * page_size
    # Retourne un tuple (start, end)
    return (start, end)
