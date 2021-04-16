import numpy as np

x = np.random.randint(1000000, size=1000)


def insertion_sort(list_a):
    indexing_lenght = range(1, len(list_a))
    for i in indexing_lenght:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -= 1

    return list_a


print(insertion_sort(x))
