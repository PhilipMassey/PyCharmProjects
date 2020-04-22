def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    p = int((hi + lo) / 2)
    pivot = arr[p]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            j = j - 1
            while arr[j] > pivot:
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]

import random
arr = random.sample(range(10),10)
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)