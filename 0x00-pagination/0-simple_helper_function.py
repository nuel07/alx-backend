#!/usr/bin/env python3
''' helper function module '''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' returns tuple '''
    start_idx = page * page_size - page_size
    stop_idx = start_idx + page_size
    return (start_idx, stop_idx)
