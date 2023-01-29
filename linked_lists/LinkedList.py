from .Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Insert a node from the forward of a linked list
    def insertAtHead(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    # Insert a node from the backward of a linked list
    def insertAtTail(self, data):
        if self.length == 0:
            return self.insertAtHead(data)

        current = self.head
        while current.pointer:
            current = current.pointer

        node = Node(data, None)
        current.pointer = node
        self.length += 1

    # Get a node in a linked list by its index
    # Time complexity: O(n) (because we need to always access the first node (head node)
    # to be able to access the other nodes
    def getNodeAtIndex(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head

        if index > 0 and index < self.length:
            current = self.head.pointer
            for i in range(1, index):
                current = current.pointer

        return current

    # Insert a node into linked list from arbitrary position
    def insertAtIndex(self, data, index):
        if index < 0:
            return None
        if index == 0:
            self.insertAtHead(data)
        if index >= self.length:
            self.insertAtTail(data)
            self.length += 1

        prevNode = self.getNodeAtIndex(index - 1)
        node = Node(data, prevNode.pointer)
        prevNode.pointer = node
        self.length += 1

    # Delete a node from forward of a linked list
    def removeAtHead(self):
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
    def removeAtTail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.removeAtHead()

        previous_last_node = self.getNodeAtIndex(self.length - 2)
        previous_last_node.pointer = None
        self.length -= 1


    # Delete a node from a linked list by its index (position)
    def removeAtIndex(self, index):
        if index < 0 or self.head == None:
            return None
        if index == 0:
            self.length -= 1
            return self.removeAtHead()
        if index >= self.length:
            self.length -= 1
            return self.removeAtTail()

        deleted_node = self.getNodeAtIndex(index)
        previous_node = self.getNodeAtIndex(index - 1)

        previous_node.pointer = deleted_node.pointer
        deleted_node.pointer = None
        self.length -= 1
