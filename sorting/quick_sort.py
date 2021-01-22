
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


print(quick_sort([1, 1, 34, 13, 4, 23, 231, 4423, 45, 43, 3, 5, 6, 5756, 5, 35, 342, 4,
                  6, 5647, 54, 23, 4, 53, 5, 656, 457, 234, 24, 5, 6, 47, 7, 86, 64, 2332, 5, 7, 5, ]))
