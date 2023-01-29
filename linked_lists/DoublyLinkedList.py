from .Node import DoublyNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Get a node in linked list by its position
    def getNodeAtIndex(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head

        current_node = self.head.next_pointer
        for i in range(1, index):
            current_node = current_node.next_pointer

        return current_node

    # Insert a node from the forward of a doubly linked list
    def insertAtHead(self, data):
        new_node = DoublyNode(None, data, self.head)
        if self.head:
            self.head.prev_pointer = new_node

        self.head = new_node
        self.length += 1

    # Insert a node from the backward of a doubly linked list
    def insertAtTail(self, data):
        if not self.head:
            return self.insertAtHead(data)

        # Get last node in a doubly linked list
        # self.getNodeAtIndex(self.length - 1)
        current_node = self.head
        while current_node.next_pointer:
            current_node = current_node.next_pointer

        # Set up new node and insert it into doubly linked list
        new_node = DoublyNode(current_node, data, None)
        current_node.next_pointer = new_node
        self.length += 1

        return

    # Insert a node at an arbitrary position in a doubly linked list
    def insertAtIndex(self, data, index):
        if index < 0:
            return None
        if index == 0:
            return self.insertAtHead(data)
        if index >= self.length:
            return self.insertAtTail(data)

        prev_node = self.getNodeAtIndex(index - 1)
        new_node = DoublyNode(prev_node, data, prev_node.next_pointer)
        prev_node.next_pointer.prev_pointer = new_node
        prev_node.next_pointer = new_node
        self.length += 1

    # Delete a doubly node from the forward of a doubly linked list
    def removeAtHead(self):
        if not self.head:
            return None

        node = self.head
        head_node = node.next_pointer

        if head_node:
            head_node.prev_pointer = None
        self.head = head_node
        self.length -= 1

        return

    # Delete a doubly node from the backward of a doubly linked list
    def removeAtTail(self):
        if not self.head:
            return None
        if self.length == 1:
            return self.removeAtHead()

        node = self.getNodeAtIndex(self.length - 2)
        node.next_pointer = None
        self.length -= 1


    # Delete a doubly node at an arbitrary position in a linked list
    def removeAtIndex(self, index):
        if not self.head or index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.removeAtHead()
        if index == self.length - 1:
            return self.removeAtTail()

        deleted_node = self.getNodeAtIndex(index)
        if deleted_node.prev_pointer:
            deleted_node.prev_pointer.next_pointer = deleted_node.next_pointer
        if deleted_node.next_pointer:
            deleted_node.next_pointer.prev_pointer = deleted_node.prev_pointer
        self.length -= 1