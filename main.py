# This is a sample Python script.

from linked_lists.LinkedList import LinkedList
from linked_lists.DoublyLinkedList import DoublyLinkedList


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insertAtHead("First")
    linked_list.insertAtHead("Second")
    linked_list.insertAtHead("Third")
    linked_list.insertAtHead("Fourth")
    linked_list.insertAtHead("Next")
    linked_list.removeAtIndex(2)
    print(linked_list.getNodeAtIndex(0).value)
    print(linked_list.getNodeAtIndex(1).value)
    print(linked_list.getNodeAtIndex(2).prev_pointer.value)
    print(linked_list.getNodeAtIndex(3).value)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
