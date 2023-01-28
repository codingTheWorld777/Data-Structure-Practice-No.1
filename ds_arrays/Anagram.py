def is_anagram(input1, input2):
    if (len(input1) != len(input2)): return False

    list_input2 = list(input2)
    for i in range(len(input1)):
        for j in range(len(list_input2)):
            if (input1[i] == list_input2[j]):
                list_input2.remove(list_input2[j])
                break
    print(list_input2)
    return len(list_input2) == 0

if __name__ == "main":
    is_anagram("restful", "fluster")