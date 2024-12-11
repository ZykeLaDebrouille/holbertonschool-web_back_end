#!/usr/bin/env python3#!/usr/bin/env python3
"""
Module for paginating a dataset of popular baby names.
"""

import csv
import math
from typing import List, Dict, Any
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
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        # Calcul des indices
        start, end = index_range(page, page_size)

        # Extraction des données
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []


    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with hypermedia information about the pagination.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing metadata about the pagination.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)    # Calcul de total_pages : Utilise math.ceil pour arrondir au supérieur. 
                                                                    # Exemple : Si le dataset contient 19419 lignes et page_size = 100, alors 
                                                                    # : \text{total_pages} = \lceil \frac{19419}{100} \rceil = 195

        return {
            "page_size": len(data),  # Nombre d'éléments sur la page actuelle
            "page": page,  # Numéro de la page actuelle
            "data": data,  # Données de la page
            "next_page": page + 1 if page < total_pages else None,  # Page suivante si supérieur à total_pages, pas de page
            "prev_page": page - 1 if page > 1 else None,  # Page précédente, si inférieur à 1, pas de page
            "total_pages": total_pages
        }
