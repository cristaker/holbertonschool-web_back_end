#!/usr/bin/env python3

"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init
        """
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
        """ return the appropriate page of the dataset (i.e. the correct
            list of rows). If the input arguments are out of range for the
            dataset, an empty list should be returned.
        """
        for param in [page, page_size]:
            assert isinstance(param, int) and page > 0
        self.dataset()
        range_pagination = index_range(page=page, page_size=page_size)
        return self.__dataset[range_pagination[0]:range_pagination[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Implement a get_hyper method that takes the same arguments (and
        defaults) as get_page and returns a dictionary containing the
        following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        records = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(records),
            'page': page,
            'data': records,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }
        