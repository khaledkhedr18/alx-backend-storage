import requests
from functools import wraps
from typing import Callable

def count_calls_and_cache(url: str, expiration_time: int) -> Callable:
    """Counts how many times a particular URL was accessed and caches the result.
    As a key, use the qualified name of the function using __qualname__.
    Create and return function
    that increments the count for that key every time the function is called
    and returns the value returned by the original function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            key = f"count:{url}"
            cache_key = f"cache:{url}"
            self._redis.incr(key)
            cached_value = self._redis.get(cache_key)
            if cached_value is not None:
                return cached_value.decode("utf-8")
            result = func(url)
            self._redis.setex(cache_key, expiration_time, result)
            return result
        return wrapper
    return decorator

@count_calls_and_cache("{url}", 10)
def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL and returns it."""
    response = requests.get(url)
    return response.text
