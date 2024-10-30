#!/usr/bin/env python3
"""
FIFO caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = self.cache_data.get(key).popitem(False)
            print(f"DISCARD: {first_in}")

    def get(self, key):
        """
        Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
