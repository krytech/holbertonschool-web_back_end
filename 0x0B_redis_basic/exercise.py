#!/usr/bin/env python3
""" 0x0B. Redis basic
"""
from typing import Callable, Optional, Union
from uuid import uuid4
import redis


class Cache:
    """ Cache class that stores an instance of the Redis client
    """
    def __init__(self):
        """ Initalize cache class. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid key, stores in Redis. """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """ Converts the data back to the desired format. """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts the data back to the desired format. """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """ Converts the data back to the desired format. """
        return self.get(key, int)
