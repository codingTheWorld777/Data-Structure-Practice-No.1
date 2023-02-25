# This is a sample Python script.
import math
import time

from linked_lists.LinkedList import LinkedList
from linked_lists.DoublyLinkedList import DoublyLinkedList
from ds_arrays.TwoPointers import two_pointers


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_head(9)
    linked_list.insert_at_head(8)
    linked_list.insert_at_head(7)
    linked_list.insert_at_head(6)
    linked_list.insert_at_head(5)
    linked_list.insert_at_head(4)
    linked_list.insert_at_head(3)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(0)

    linked_list.reverse()
    node = linked_list.get_head_node()
    while node:
        print(node.value, node.pointer)
        node = node.pointer

    # print(specialArray([0,4,3,0,4]))
    # print(pivotIndex([-1,-1,-1,-1,-1,-1]))
    # print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
    # print(peakIndexInMountainArray([3, 9, 10, 11, 8, 6, 4]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/