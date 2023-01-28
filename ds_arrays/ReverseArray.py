def reverse(array):
    arr_length = len(array)

    # 1
    # for i in range(0, math.floor(arr_length / 2)):
    #     item = array[i]
    #     reversed_item = array[arr_length - i - 1]
    #     print(item, reversed_item)
    #
    #     array[i] = reversed_item
    #     array[arr_length - i - 1] = item

    # 2
    low_index = 0
    high_index = arr_length - 1
    while (low_index < high_index):
        array[low_index], array[high_index] = array[high_index], array[low_index]
        low_index += 1
        high_index -= 1

    return array

if __name__ == "main":
    print(reverse([1, 2, 3, 4, 5]))