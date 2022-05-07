#!/usr/bin/env python3
''' a FIFO caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' represents a FIFO cache class '''
    def __init__(self):
        super().__init__()
        self.my_keys = []

    def put(self, key, item):
        ''' assigns to the dictionary the item value for the key '''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_this = self.my_keys.pop(0)
                del self.cache_data[discard_this]
                print("DISCARD:", discard_this)

            self.cache_data[key] = item
            self.my_keys.append(key)

    def get(self, key):
        ''' return value linked to key '''
        if key is not None:
            return self.cache_data.get(key)
