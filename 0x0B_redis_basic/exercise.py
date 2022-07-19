#!/usr/bin/env python3
""" 0x0B. Redis basic
"""
from functools import wraps
from typing import Callable, Optional, Union
from uuid import uuid4
from grpc import Call
import redis


def count_calls(method: Callable) -> Callable:
    """ Counts how many times methods of Cache class are called.
    """
    method_name = method.__qualname__
    @wraps(method)

    def counter(self, data):
        """ Increment counter. """
        self._redis.incr(method_name)
        return method(self, data)
    return counter


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs for a patricular function.
    """
    method_name = method.__qualname__
    @wraps(method)

    def history(self, data):
        """ Stores the history of inputs and outputs. """
        self._redis.rpush(method_name + ":inputs",
                          "('" + str(data) + "',)")
        self._redis.rpush(method_name + ":outputs", method(self, data))
        return method(self, data)
    return history


class Cache:
    """ Cache class that stores an instance of the Redis client.
    """
    def __init__(self):
        """ Initalize cache class. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
