# Data structure 2: Linked lists

## 1. Simple linked list
- A node in linked list store its data and the reference pointing to the next node
### Some operations with simple linked list
- Insert a node from the forward of a linked list (O(1) running time complexity)
- Insert a node from the backward of a linked list (O(n) running time complexity because we need to traverse all the nodes in this linked list)
- Remove a node from the forward of a linked list (O(1) running time complexity such as inserting from the forward)
- Remove a node from the backward of a linked list (O(n) running time complexity such as inserting a node from the backward)
- Insert a node at an arbitrary position in a linked list (O(n) because we need to traverse all the nodes in linked list)

## 2. Doubly linked list
- A node in doubly linked list store its data and the references poiting to the next node and also to the previous node
### Some operations with simple linked list
- Insert a node from the forward of a linked list (O(1) running time complexity)
- Insert a node from the backward of a linked list (O(1) running time complexity)
- Remove a node from the forward of a linked list (O(1) running time complexity)
- Remove a node from the backward of a linked list (O(1) running time complexity)
- Insert a node at an arbitrary position in a linked list (O(n) because we need to traverse all the nodes in linked list)

## 3. Some practices of linked list
- Finding the middle node in a linked list (**using 2 pointers -> ```fast_pointer = slow_pointer * 2```**)
- Reverse a linked list

## 4. Summary: Some basic algorithm operations in linked lists
- Insert a node at the beginning and at the end
- Remove a node from the beginning and from the end
- Find a node at a position
- Find the middle node
- Reverse a linked list