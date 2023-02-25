from .Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head_node(self):
        return self.head

    # Insert a node from the forward of a linked list
    def insert_at_head(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    # Insert a node from the backward of a linked list
    def insert_at_tail(self, data):
        if self.length == 0:
            return self.insert_at_head(data)

        current = self.head
        while current.pointer:
            current = current.pointer

        node = Node(data, None)
        current.pointer = node
        self.length += 1

    # Get a node in a linked list by its index
    # Time complexity: O(n) (because we need to always access the first node (head node)
    # to be able to access the other nodes
    def get_node_at_index(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head

        if 0 < index < self.length:
            current = self.head.pointer
            for i in range(1, index):
                current = current.pointer

        return current

    # Insert a node into linked list from arbitrary position
    def insert_at_index(self, data, index):
        if index < 0:
            return None
        if index == 0:
            self.insert_at_head(data)
        if index >= self.length:
            self.insert_at_tail(data)
            self.length += 1

        prevNode = self.get_node_at_index(index - 1)
        node = Node(data, prevNode.pointer)
        prevNode.pointer = node
        self.length += 1

    # Delete a node from forward of a linked list
    def remove_at_head(self):
        if self.length == 0: return None
        if self.length == 1:
            self.head.pointer = None
            self.head = None
            self.length = 0

        node = self.head.pointer
        self.head.pointer = None
        self.head = node
        self.length -= 1

    # Delete a node from backward of a linked list
    def remove_at_tail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.remove_at_head()

        previous_last_node = self.get_node_at_index(self.length - 2)
        previous_last_node.pointer = None
        self.length -= 1


    # Delete a node from a linked list by its index (position)
    def remove_at_index(self, index):
        if index < 0 or self.head == None:
            return None
        if index == 0:
            self.length -= 1
            return self.remove_at_head()
        if index >= self.length:
            self.length -= 1
            return self.remove_at_tail()

        deleted_node = self.get_node_at_index(index)
        previous_node = self.get_node_at_index(index - 1)

        previous_node.pointer = deleted_node.pointer
        deleted_node.pointer = None
        self.length -= 1

    # Find the middle node in a linked list
    def get_middle_node(self):
        if self.length:
            return None

        slow_pointer, fast_pointer = 1, 1
        node = self.head

        # fast_pointer = slow_pointer * 2, when fast_pointer reaches the end of the linked list
        # then slow_pointer reaches the middle of the linked list
        while fast_pointer <= self.length - 1:
            node_ = node
            node = node.pointer
            count = 0
            while count <= fast_pointer - slow_pointer and node_.pointer:
                node_ = node_.pointer
                count += 1
            slow_pointer += 1
            fast_pointer = slow_pointer * 2
        return node

    # Reverse a linked list
    def reverse(self):
        if self.length <= 1:
            return self.head

        current_node = self.head
        prev_node, next_node = None, None
        while current_node:
            next_node = current_node.pointer
            current_node.pointer = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node