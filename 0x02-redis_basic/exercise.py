#!/usr/bin/env python3
'''Task 0
'''
import redis
import uuid
from typing import Union


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
