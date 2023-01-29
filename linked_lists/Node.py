class Node:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

class DoublyNode:
    def __init__(self, prev_pointer, value, next_pointer):
        self.prev_pointer = prev_pointer
        self.value = value
        self.next_pointer = next_pointer

