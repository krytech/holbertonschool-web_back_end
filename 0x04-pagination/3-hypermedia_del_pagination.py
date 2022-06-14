#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Return a dictionary with: index, net_index, page_size, data"""
        index_dataset = self.indexed_dataset()

        assert isinstance(index, int) and index < (len(index_dataset) - 1)

        scout = 0
        idx = index
        data = []

        while (scout < page_size and index < len(index_dataset)):
            value = index_dataset.get(idx, None)
            if value:
                data.append(value)
                scout += 1
            idx += 1

        next_index = None
        while (idx < len(index_dataset)):
            value = index_dataset.get(idx, None)
            if value:
                next_index = idx
                break
            idx += 1

        hyper = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
        return hyper
