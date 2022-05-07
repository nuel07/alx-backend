#!/usr/bin/python3
"""
LIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ represents lifo caching class """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.my_keys = []

    def put(self, key, item):
        """ assign item to key """
        if key is not None and item is not None:
            if self.cache_data.get(key) is None:
                self.my_keys.append(key)
            else:
                self.my_keys.remove(key)
                self.my_keys.append(key)
            self.cache_data[key] = item
        if len(self.my_keys) > BaseCaching.MAX_ITEMS:
            print('DISCARD:', self.my_keys[BaseCaching.MAX_ITEMS - 1])
            self.cache_data.pop(self.my_keys[BaseCaching.MAX_ITEMS - 1])
            self.my_keys.pop(BaseCaching.MAX_ITEMS - 1)

    def get(self, key):
        """ return value of key """
        if key is not None:
            return self.cache_data.get(key)
