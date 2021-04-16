
import numpy as np

x = np.random.randint(1000000, size=1000)


def quick_sort(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort(x))
