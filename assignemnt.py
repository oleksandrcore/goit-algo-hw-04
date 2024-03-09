import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def timsort(arr):
    return sorted(arr)


# Генеруємо випадковий набір даних
data = [random.randint(0, 100) for _ in range(100)]

merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=100)
insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=100)
timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=100)

# Виводимо результати
print("Merge Sort time:", merge_sort_time)
print("Insertion Sort time:", insertion_sort_time)
print("Timsort time:", timsort_time)