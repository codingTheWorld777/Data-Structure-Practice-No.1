# This is a sample Python script.

import time

from linked_lists.LinkedList import LinkedList
from linked_lists.DoublyLinkedList import DoublyLinkedList


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Start")
    now = time.time()
    array = []
    linked_lists = DoublyLinkedList()

    for i in range(0, 500000):
        array.append(i)

    print("Inserting items into array in %ss" % str(time.time() - now))

    now = time.time()
    for i in range(0, 500000):
        linked_lists.insertAtTail(i)

    print("Inserting items into linked list in %ss" % str(time.time() - now))
    # linked_list = DoublyLinkedList()
    # linked_list.insertAtTail("First")
    # linked_list.insertAtTail("Second")
    # linked_list.insertAtHead("1")
    # linked_list.insertAtHead("2")
    # linked_list.removeAtIndex(2)
    # print(linked_list.getNodeAtIndex(0).value)
    # print(linked_list.getNodeAtIndex(1).value)
    # print(linked_list.getNodeAtIndex(2).value)
    # # print(linked_list.getNodeAtIndex(3).value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
