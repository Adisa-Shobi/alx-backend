#!/usr/bin/env python3
'''
a function named index_range that takes two integer
arguments page and page_size.
'''
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
        '''
        return paginated data
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        (begin, end) = index_range(page, page_size)
        data = self.dataset()
        if end > len(data):
            return []
        return data[begin:end]


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters
    '''
    offset = page * page_size
    return (offset - page_size, offset)
