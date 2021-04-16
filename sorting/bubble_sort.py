import numpy as np

x = np.random.randint(1000000, size=1000)


def bubble_sort(list_a):
    indexing_lenght = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_lenght):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a


print(bubble_sort(x))
