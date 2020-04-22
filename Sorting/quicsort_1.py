import random

arr = random.sample(range(10), 10)
arr = [5, 1, 0, 4, 9, 3, 6, 2, 8, 7]
print(arr)


def partition(sort_list, low, high):
    i = (low - 1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            if i == j: continue
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[high] = sort_list[high], sort_list[i + 1]
    print(sort_list)
    return (i + 1)


def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        print(pi,sort_list)
        quick_sort(sort_list, low, pi - 1)
        print(pi,sort_list)
        quick_sort(sort_list, pi + 1, high)


quick_sort(arr, 0, len(arr) - 1)
print(arr)