#!/usr/bin/env python3
""" 2. Hypermedia pagination """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset_records = self.get_page(page, page_size)
        page_dict = math.ceil(len(self.__dataset) / page_size)

        hyper = {
            'page_size': page_size,
            'page': page,
            'data': dataset_records,
            'next_page': page + 1 if (page + 1) <= page_dict else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': page_dict
        }
        return hyper


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
