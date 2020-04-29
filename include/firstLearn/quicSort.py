def quick_sort(array, low, high):
    if low < high:
        instance = get_instance(array, low, high)
        quick_sort(array, low, instance - 1)
        quick_sort(array, instance + 1, high)


def get_instance(array, low, high):
    while low < high:
        temp = array[low]
        while low < high and temp <= array[high]:
            high -= 1
        array[low] = array[high]
        while low < high and temp >= array[low]:
            low += 1
        array[high] = array[low]
    array[low] = temp
    return low


array = [123, 235, 6, 4, 123, 65, 7, 234]
quick_sort(array, 0, len(array) - 1)
print(array)
