#!/usr/bin/python3
"""
LFU caching system
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    Represents a cache class based on LRU (least frequently used)
    """

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.my_keys = []
        self.usage = {}

    def put(self, key, item):
        ''' assign to the dictionary self.cache_data
        the item value for the key key '''

        if key is not None and item is not None:
            if (len(self.my_keys) == BaseCaching.MAX_ITEMS and
                    key not in self.my_keys):
                discard_this = self.my_keys.pop(
                    self.my_keys.index(self.findLFU()))
                del self.cache_data[discard_this]
                del self.usage[discard_this]
                print('DISCARD: {:s}'.format(discard_this))
            self.cache_data[key] = item
            if key not in self.my_keys:
                self.my_keys.append(key)
                self.usage[key] = 0
            else:
                self.my_keys.append(self.my_keys.pop(
                    self.my_keys.index(key)))
                self.usage[key] += 1

    def get(self, key):
        ''' Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            self.my_keys.append(
                self.my_keys.pop(self.my_keys.index(key)))
            self.usage[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        ''' Returns the key of least frequently used item in cache.
            If multiple items have the same amount of uses, it will return
            the least recently used one.
        '''
        items = list(self.usage.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.my_keys:
            if key in lfus:
                return key
