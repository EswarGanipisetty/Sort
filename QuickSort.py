def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        return None
    quicksort(arr, 0, len(arr) - 1)
    return arr[i]

# Example usage:
arr = [12, 3, 5, 7, 4, 19, 26]
i = 3  # Find the 3rd order statistic (0-indexed)
ith_statistic = ith_order_statistic(arr, i)
print(f"The {i+1}th order statistic is: {ith_statistic}")


#output
#The 4th order statistic is: 7

