import unittest
import random  # Import the random module
from randomized_quicksort import randomized_quicksort, deterministic_quicksort

def time_quicksort(func, arr):
    import time
    start = time.time()
    func(arr, 0, len(arr) - 1)
    return time.time() - start

class TestRandomizedQuicksort(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [1]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        arr = [4, 2, 4, 2, 4]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [2, 2, 4, 4, 4])

    def test_comparison(self):
        arr_sizes = [100, 1000, 10000]
        for size in arr_sizes:
            arr = [random.randint(0, 100000) for _ in range(size)]
            arr_copy = arr.copy()

            rand_time = time_quicksort(randomized_quicksort, arr)
            det_time = time_quicksort(deterministic_quicksort, arr_copy)

            print(f"Array size: {size} | Randomized Time: {rand_time:.5f}s | Deterministic Time: {det_time:.5f}s")

if __name__ == "__main__":
    unittest.main()
