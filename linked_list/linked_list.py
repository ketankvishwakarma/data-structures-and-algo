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
            return None
        # if only one is there:
        previous = self.head
        current = self.head
        while current.next!=None:
            previous = current
            current = current.next
        print("poping {} ".format(current.data))
        previous.next = None
        self.tail = previous
        self.lenght-=1
        return current

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
    
    def get(self,postion):
        if postion <= 0 or postion > self.lenght:
            return None
        node = self.head
        for i in range(postion-1):
            node = node.next
        return node

    def insert(self,value,position):
        if position <= 0 or position > self.lenght:
            return None
        if value == None:
            return None
        pre = self.head
        swap_node = self.head
        current_postion = 1
        while current_postion<position:
            pre = swap_node
            swap_node = swap_node.next
            current_postion+=1
        new_node = Node(value)
        pre.next = new_node
        new_node.next = swap_node
        self.lenght+=1
        




    def print(self):
        print("list of {} node | [{}]".format(self.lenght,self.head))


s = SinglyLinkedList()

[s.push(i) for i in range(10)]

s.print()

#print(s.get(5))
#print(s.get(0))
#print(s.get(1))
#s.pop()
#s.print()
s.insert(100,7)
s.print()
print(s.get(7))
print(s.get(1))