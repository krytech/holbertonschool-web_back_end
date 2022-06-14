#!/usr/bin/env python3
""" 1. Simple pagination """
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns list with page from dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        self.dataset()
        if self.__dataset is None:
            return []

        pagination_index = index_range(page, page_size)
        return self.__dataset[pagination_index[0]: pagination_index[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
