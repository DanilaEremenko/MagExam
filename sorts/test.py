import unittest
import os
import numpy as np
from sorts.algorithms import *

os.chdir(os.getcwd() + "/..")


def test_one(arr, right_arr, sort_func):
    result = sort_func(arr)
    assert result == right_arr


class SortTest(unittest.TestCase):
    def setUp(self):
        self.arr = list(np.random.uniform(low=0, high=1000, size=(10_000,)))
        self.right_arr = sorted(self.arr)

    def test_bubble(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=bubble_sort)

    def test_selection(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=selection_sort)

    def test_insertion(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=insertion_sort)

    def test_merge(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=merge_sort)

    def test_quick(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=quick_sort)

    def test_default(self):
        test_one(arr=self.arr, right_arr=self.right_arr, sort_func=default_sort)
