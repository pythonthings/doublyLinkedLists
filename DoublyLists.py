'''
This is a Doubly Linked List in python
Functions
- push: adds to front of the list
- print_list: displays list in order and in revesed order
- insert_after: point new node to previous node and the node after the previous with previous pointer and next pointers
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = prev = None
        self.next = next = None

class Lists:
    def __init__(self):
        self.head = None

    def push(self,data):
        #push new node to front of the list
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self,prev_node,data):
        if prev_node is None:
            print('No previous node')
            return
        new_node = Node(data)
        #point next of new_node to the next node of previous
        new_node.next = prev_node.next
        #point previous node to the new node
        prev_node.next = new_node
        #point new node previous to previous node
        new_node.prev = prev_node
        if new_node.next is not None:
            #point the node after the new nodes previous pointer back to the new node
            new_node.next.prev = new_node

    def append(self,data):
        new_node = Node(data)
        #set the next of the new node to none since it will be the new tail node
        new_node.next = None
        #if list is empty node is the new head
        if self.head is None:
            self.head = new_node

        #get the last node
        find_last = self.head
        while(find_last.next):
            find_last = find_last.next
        #point last node to new node
        find_last.next = new_node
        new_node.prev = find_last

    def print_list(self):
        node = self.head
        print('In order: ')
        while(node):
            print(node.data)
            #used to get the last node to print in reversed order
            find_last = node
            node = node.next
        print('Reversed order: ')
        #uses the last node from in order iteration to point from tail using the prev pointer all the way to the head
        while(find_last):
            print(find_last.data)
            find_last = find_last.prev
