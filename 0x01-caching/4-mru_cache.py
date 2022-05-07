#!/usr/bin/env python3
''' MRU caching system '''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' represents MRU cache class '''
    def __init__(self):
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        ''' assigns to dictionary item value for the key '''
        if not key or not item:
            return

        self.cache_data[key] = item
        self.cache_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_this = next(iter(self.cache_order))
            del self.cache_data[discard_this]
            print("DISCARD:", discard_this)

        if len(self.cache_order) > BaseCaching.MAX_ITEMS:
            self.cache_order.popitem(last=False)

        self.cache_order.move_to_end(key, False)

    def get(self, key):
        ''' self descriptive '''
        if key in self.cache_data:
            self.cache_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
