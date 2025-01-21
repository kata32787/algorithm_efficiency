import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with the last element
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot - 1)
        randomized_quicksort(arr, pivot + 1, high)

if __name__ == "__main__":
    # Example test case
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    randomized_quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot - 1)
        deterministic_quicksort(arr, pivot + 1, high)
