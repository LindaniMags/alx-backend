#!/usr/bin/env python3
"""
LFU Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """
        Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")
