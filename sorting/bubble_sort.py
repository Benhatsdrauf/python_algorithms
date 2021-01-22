
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


print(bubble_sort([2, 5, 3246, 4, 3, 4, 6, 7, 8, 8,
                   5, 346, 56, 865, 58, 2345, 435, 7, 65, 84]))
