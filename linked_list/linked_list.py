class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    def __str__(self) -> str:
        return "{} --> {}".format(self.data,self.next)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def pop(self):
        if self.head == None:
            return False
        # if only one is there:
        previous = self.head
        current = self.head
        while current.next!=None:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        self.lenght-=1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return True

    def push(self,value):
        new_node = Node(value)
        # is list is empty then add 
        if self.head==None:
            self.head = new_node
            self.tail = new_node
            self.lenght +=1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.lenght+=1
        return True
    
    def get(self,postion):
        if postion <= 0 or postion > self.lenght:
            return None
        node = self.head
        for i in range(postion-1):
            node = node.next
        return node

    def set(self,value,index):
        returned_value = self.get(index)
        if returned_value != None:
            returned_value.data = value
            return True
        return False

    def insert(self,value,position):
        if value == None:
            return False
        if position <= 0 or position > self.lenght:
            return False
        if position == self.lenght:
            self.push(value)
            return True

        pre = self.head
        swap_node = self.head
        current_postion = 1
        while current_postion < position:
            pre = swap_node
            swap_node = swap_node.next
            current_postion+=1
        new_node = Node(value)
        if position==1:
            new_node.next = self.head
            self.head = new_node
        else:
            pre.next = new_node
            new_node.next = swap_node
        self.lenght+=1
        return True
        
    def remove(self,position):
        if position == 0 or position > self.lenght:
            return False
        if self.lenght == 1 or position == self.lenght:
            return self.pop()
        
        current = self.head
        previous = self.head
        for i in range(1,position):
            previous = current
            current = current.next

        next_item = current.next
        previous.next = next_item
        current.next = None
        self.lenght-=1
        if position == 1:
            self.head = next_item
        return True

    def reverse(self):

        if self.lenght <=1:
            return True
        
        node = self.head
        self.head = self.tail
        self.tail = node
        pre = None
        next_node = None
        for i in range(self.lenght):
            next_node = node.next
            node.next = pre
            pre = node
            node = next_node 



    def print(self):
        print("list of {} node | [{}]".format(self.lenght,self.head))


s = SinglyLinkedList()

[s.push(i) for i in range(1,6)]

s.print()

s.reverse()

s.print()

""" remove """
#print("removing 0th item {}".format(s.remove(0)))
#s.print()
#print("removing 1th item {}".format(s.remove(1)))
#s.print()
#print("removing 5th item {}".format(s.remove(5)))
#s.print()
#print("removing 6th item {}".format(s.remove(6)))
#s.print()
#print("removing 7th item {}".format(s.remove(7)))



