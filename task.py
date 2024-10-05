import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def python_sort(arr):
    return sorted(arr)


def test_sorting_algorithms():
    sizes = [1000, 5000, 10000] 
    types = ["sorted", "reversed", "random"]

    for size in sizes:
        for data_type in types:
            if data_type == "sorted":
                arr = list(range(size))
            elif data_type == "reversed":
                arr = list(range(size, 0, -1))
            else: 
                arr = random.sample(range(size * 10), size)

            print(f"\nSize: {size}, Type: {data_type}")

            insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
            print(f"Insertion Sort: {insertion_time:.5f} seconds")

            merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
            print(f"Merge Sort: {merge_time:.5f} seconds")

            timsort_time = timeit.timeit(lambda: python_sort(arr.copy()), number=1)
            print(f"Python Sort (Timsort): {timsort_time:.5f} seconds")

test_sorting_algorithms()