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
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def print_linkd_list(linked_list):
    current_node = linked_list.head
    while(current_node is not None):
        print("--> {}".format(current_node.value))
        current_node = current_node.next


def remove_dublicate(l_list):
    current_node = l_list.head
    while(current_node is not None):
        temp = current_node.next
        while(temp is not None and temp.value == current_node.value):
            temp = temp.next
        current_node.next = temp
        current_node = temp


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

print_linkd_list(list)
print("after removal of duplicates")
remove_dublicate(list)
print_linkd_list(list)
