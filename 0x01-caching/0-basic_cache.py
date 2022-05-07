#!/usrr/bin/env python3
''' a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' represents a Base cache class '''
    def put(self, key, item):
        '''assigns item to key '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' returns value linked to key '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
