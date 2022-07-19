#!/usr/bin/env python3
""" 0x0B. Redis basic
"""
from typing import Union
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
        """ Generates a random uuid key. """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
