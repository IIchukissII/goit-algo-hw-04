import timeit
import random
import numpy as np
import matplotlib.pyplot as plt


def insertion_sort(lst):
    start = timeit.default_timer()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    end = timeit.default_timer()
    return len(lst), round(end - start, 1)


def merge_sort(lst):
    start = timeit.default_timer()
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
    end = timeit.default_timer()
    return len(lst), round(end - start, 1)


def time_sort(lst):
    start = timeit.default_timer()
    lst.sort()
    end = timeit.default_timer()
    return len(lst), round(end - start, 1)


def make_polynom(data):
    poly = np.polyfit(data[:, 0], data[:, 1], 2)
    return poly


def create_plot_data(poly):
    x = np.linspace(0, 10000000, 10000000)
    y = np.polyval(poly, x)
    return x, y


insert_data = np.zeros((0, 2))
for i in range(0, 10000, 1000):
    lst = random.sample(range(i), i)
    sorted_lst = insertion_sort(lst)
    insert_data = np.vstack((insert_data, sorted_lst))
insert_poly = make_polynom(insert_data)
x_insert, y_insert = create_plot_data(insert_poly)

merge_data = np.zeros((0, 2))
for i in range(0, 1000000, 100000):
    lst = random.sample(range(i), i)
    sorted_lst = merge_sort(lst)
    merge_data = np.vstack((merge_data, sorted_lst))
merge_poly = make_polynom(merge_data)
x_merge, y_merge = create_plot_data(merge_poly)


timeit_data = np.zeros((0, 2))
for i in range(0, 1000000, 10000):
    lst = random.sample(range(i), i)
    sorted_lst = time_sort(lst)
    timeit_data = np.vstack((timeit_data, sorted_lst))
timeit_poly = make_polynom(timeit_data)
x_timeit, y_timeit = create_plot_data(timeit_poly)

plt.semilogy(x_merge, y_merge, label="Merge sort")
plt.semilogy(x_insert, y_insert, label="Insert sort")
plt.semilogy(x_timeit, y_timeit, label="Timsort")
plt.xlabel("Number of elements")
plt.ylabel("Time, [seconds]")
plt.grid(True)
plt.legend()
plt.show()
