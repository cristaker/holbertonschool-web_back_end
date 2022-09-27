#!/usr/bin/env python3

"""
1. Simple pagination
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
    