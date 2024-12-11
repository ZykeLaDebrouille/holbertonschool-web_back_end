#!/usr/bin/env python3
"""
Module for paginating a dataset of popular baby names.
"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Ignore the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page of the dataset.
        """
        # Validation des arguments
        assert isinstance(page, int) and page > 0, "must be positive int"
        assert isinstance(page_size, int) and page_size > 0, "must be positive"

        # Calcul des indices
        start, end = index_range(page, page_size)

        # Extraction des données
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []
