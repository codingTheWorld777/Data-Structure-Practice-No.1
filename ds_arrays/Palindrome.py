def is_palindrome(str):
    # 1
    # if str == str[::-1]: return True
    # else: return False

    # 2
    str_length = len(str)
    low_index = 0
    high_index = str_length - 1

    while low_index < high_index:
        if str[low_index] != str[high_index]:
            return False
        else:
            low_index += 1
            high_index -= 1

    return True

if __name__ == "main":
    print(is_palindrome("radar"))
    print(is_palindrome("mvvm"))
    print(is_palindrome("false"))