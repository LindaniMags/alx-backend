#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        ensures user does not miss items from dataset when changing page.
        """
        i_dataset = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(
            i_dataset.keys())
        count = 0
        data = []
        next_index = None
        start_idx = index if index else 0
        for i, item in i_dataset.items():
            if i >= start_idx and count < page_size:
                data.append(item)
                count += 1
                continue
            if count == page_size:
                next_index = i
                break
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }
