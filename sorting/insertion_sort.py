

def insertion_sort(list_a):
    indexing_lenght = range(1, len(list_a))
    for i in indexing_lenght:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -= 1

    return list_a


print(insertion_sort([12, 5, 2, 78, 5, 345, 2, 5, 8, 79,
                      9, 78, 53, 4, 231, 54, 2, 45, 46, 3, 23, 6, 5]))
