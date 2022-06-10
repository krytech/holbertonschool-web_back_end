#!/usr/bin/python3
""" 0. Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """ assign item for key in cache_data """
        if  key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ return value of cache_data linked to key """
        if key is None:
            return
        return self.cache_data.get(key, None)
