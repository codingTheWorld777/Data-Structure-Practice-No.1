def calculate_trapped_water(input):
    if len(input) < 3:
        return 0

    result = 0
    max_left_values = [0]   # By convention, first item of list has its maximum left value equals to 0
    max_right_values = [0]  # By convention, last item of list has its maximum right value equals to 0
    max_value = 0

    # Find max_left_values associated with each item in list
    for i in range(1, len(input)):
        if input[i - 1] > max_value:
            max_value = input[i - 1]
        max_left_values.append(max_value)

    # Find max_right_values associated with each item in list
    max_value = 0
    for i in range(len(input) - 2, -1, -1):
        if input[i + 1] > max_value:
            max_value = input[i + 1]
        max_right_values.insert(0, max_value)

    # Calculate trapped water of each position of item
    for i in range(len(input)):
        trapped_water = min(max_left_values[i], max_right_values[i]) - input[i]
        if trapped_water > 0:
            result += trapped_water

    return result

if __name__ == "main":
    print(calculate_trapped_water([4, 1, 3, 1, 5]))
    print(calculate_trapped_water([1, 0, 2, 1, 3, 1, 2, 0, 3]))
