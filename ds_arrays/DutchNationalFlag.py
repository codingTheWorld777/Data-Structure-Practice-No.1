# DUTCH NATIONAL FLAG PROBLEM
# Requirement: O(n) and using constant memory

# Swap 2 items in an array
def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]

def dutch_sort_desc(arr, pivot=1):
    i = 0 # i tracks left cluster index
    j = 0 # j tracks actual item
    k = len(arr) - 1 # k tracks right cluster index

    while (j <= k):
        if arr[j] < pivot:
            swap(arr, j, k)
            k -= 1
        elif arr[j] > pivot:
            swap(arr, j, i)
            i += 1
            j += 1
        else:
            j += 1

    return arr

def dutch_sort_asc(arr, pivot=1):
    i = 0
    j = 0
    k = len(arr) - 1

    while j <= k:
        if arr[j] > pivot:
            swap(arr, j, k)
            k -= 1
        elif arr[j] < pivot:
            swap(arr, j, i)
            i += 1
            j += 1
        else:
            j += 1

    return arr

if __name__ == "main":
    print(dutch_sort_desc([2, 2, 0, 0, 1, 2, 2, 0, 1, 0, 2]))
    print(dutch_sort_asc([2, 2, 0, 0, 1, 2, 2, 0, 1, 0, 2]))