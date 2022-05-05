#!/usr/bin/env python3
#!/usr/bin/env python3
'''  A simple pagination module '''

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self):
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]


        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''returns a list'''
        self.dataset()
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0
        idx = index_range(page, page_size)
        if len(self.__dataset) <= idx[0]:
            return []

        return self.__dataset[idx[0]:idx[1]]

    def get_hyper(self, page: int=1, page_size: int=10) -> Dict:
        ''' returns a dictionary '''
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        page_dict = {
            "page": page,
            "page_size": page_size if page < total_pages else 0,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
            }
        return page_dict

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' returns  tuple '''
    start_idx = page * page_size - page_size
    stop_idx = start_idx + page_size
    return (start_idx, stop_idx)
