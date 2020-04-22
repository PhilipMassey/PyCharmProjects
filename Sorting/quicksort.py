import random

arr = random.sample(range(10), 10)
arr = [9, 7, 8, 4, 1, 3, 6, 2, 5, 0]
print(arr)


def quick_sort(arr, lo, hi, par):
    if lo >= hi:
        print('lo',lo,'hi',hi,'w00')
    if lo < hi:
        print('lo',lo,'hi',hi,par,arr)
        p = partition(arr, lo, hi)
        print('p',p,arr[p])
        quick_sort(arr, lo, p - 1, 'aaa')
        quick_sort(arr, p + 1, hi,'bbb')


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


quick_sort(arr, 0, len(arr) - 1,'---')
print(arr)