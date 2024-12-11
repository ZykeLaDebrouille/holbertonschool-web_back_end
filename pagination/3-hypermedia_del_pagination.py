#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination metadata that handles deletions.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: Metadata about the current page and dataset state.
        """
 # Vérifier que l'index demandé est valide (entre 0 et la taille du dataset indexé)
        assert index is not None and 0 <= index < len(self.indexed_dataset()), \
            "Index out of range."

        # Initialiser les variables pour collecter les données de la page
        data = []  # Stocke les données de la page
        current_index = index  # Index actuel à partir duquel commencer
        indexed_data = self.indexed_dataset()  # Récupérer le dataset indexé
        keys = list(indexed_data.keys())  # Obtenir toutes les clés valides

        # Parcourir les clés pour collecter les éléments jusqu'à atteindre la taille de la page
        while len(data) < page_size and current_index < len(keys):
            if current_index in indexed_data:  # Si l'index actuel est encore valide
                data.append(indexed_data[current_index])  # Ajouter la donnée correspondante
            current_index += 1  # Passer à l'index suivant

        # Déterminer l'index pour la page suivante (ou None si on a atteint la fin)
        next_index = current_index if current_index < len(keys) else None

        # Retourner les métadonnées et les données
        return {
            "index": index,  # Index de départ pour cette page
            "data": data,  # Données de la page
            "page_size": len(data),  # Nombre d'éléments dans la page
            "next_index": next_index  # Index pour la page suivante (None si fin du dataset)
        }
    