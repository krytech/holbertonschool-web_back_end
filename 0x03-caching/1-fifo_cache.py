#!/usr/bin/python3
""" 1. FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_off = sorted(self.cache_data)[0]
            self.cache_data.pop(pop_off)
            print('DISCARD: {}'.format(pop_off))

    def get(self, key):
        """ return value of cache_data linked to key """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
