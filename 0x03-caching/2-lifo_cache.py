#!/usr/bin/python3
""" 2. LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """ return value of cache_data linked to key """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
