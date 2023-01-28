from ReverseArray import reverse

def reverse_int(integer):
    reversed_int = 0

    while integer > 0:
        remainder = integer % 10
        reversed_int = reversed_int * 10 + remainder
        integer = integer // 10

    return reversed_int

if __name__ == "main":
    print(reverse_int(1234))