from hashlib import new
from threading import currentThread


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print_list(self):
        if self.head is None:
            print("list is empty")
            return
        pl = []
        current_node = self.head
        while(current_node is not None):
            val = current_node.value
            pl.append(val)
            current_node = current_node.next
        print(pl)

def remove_dublicate(l_list):
    current_node = l_list.head
    while(current_node is not None):
        next_distinct = current_node.next
        while(next_distinct is not None and next_distinct.value == current_node.value):
            next_distinct = next_distinct.next
        current_node.next = next_distinct
        current_node = next_distinct

def reverse(l_list):
    previous_node = None
    current_node = l_list.head
    while(current_node is not None):
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    l_list.head = previous_node


def reverse_new(l):
    previos_node = None
    current_node = l.head
    while(current_node is not None):
        next_node = current_node.next
        current_node.next = previos_node
        previos_node = current_node
        current_node = next_node
    l.head = previos_node
    



list = LinkedList()
list.add(1)
list.add(1)
list.add(3)
list.add(4)
list.add(4)
list.add(4)
list.add(5)
list.add(6)
list.add(6)

list.print_list()

remove_dublicate(l_list=list)
list.print_list()

reverse(l_list=list)
list.print_list()

reverse_new(l=list)
list.print_list()