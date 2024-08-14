#!/usr/bin/env python3
'''Task 0, 1, 2, 3,
'''
import functools
import redis
import uuid
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class are called.
    As a key, use the qualified name of method using __qualname__.
    Create and return function
    that increments the count for that key every time the method is called
    and returns the value returned by the original method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """History of inputs and outputs for a particular function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"
        self._redis.rpush(key_inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, str(result))
        return result
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes a new instance of the Cache class.
        This method creates a new Redis client and flushes the Redis database.
        Parameters:
            None
        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the Redis database.
        Parameters:
            data (Union[str, bytes, int, float]): The data to be stored.
        Returns:
            str: A unique key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None):
        """
        Retrieves data from the Redis database.
        Parameters:
            key (str): The key to retrieve data from.
            fn (callable): An optional callable to convert
                            the data to the desired type.
        Returns:
            The retrieved data.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str):
        """
        Retrieves a string from the Redis database.
        Parameters:
            key (str): The key to retrieve data from.
        Returns:
            str: The retrieved string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """
        Retrieves an integer from the Redis database.
        Parameters:
            key (str): The key to retrieve data from.
        Returns:
            int: The retrieved integer.
        """
        return self.get(key, fn=int)
