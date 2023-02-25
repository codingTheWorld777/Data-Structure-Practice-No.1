"""
Condition: a sorted array in ascending order (increase strictly)
"""
def two_pointers(arr, T):
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        sum = arr[left] + arr[right]
        if sum < T:
            left += 1
        elif sum > T:
            right -= 1
        else:
            result.append((arr[left], arr[right]))
            left += 1
            right -= 1
    return result