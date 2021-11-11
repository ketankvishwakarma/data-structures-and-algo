
from typing import Any


class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
    def __str__(self) -> str:
        return "{} --> {}".format(self.data,self.next)


class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.head = None

    def push(self,value) -> Node:
        print("pushing {}".format(value))
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.size +=1
        else:
            tmp = self.head
            self.head = node
            node.next = tmp
            self.size +=1
    
    def pop(self) -> Any:
        print("popping")
        node_to_return = None
        if self.size == 0:
            return node_to_return
        else:
            node_to_return = self.head
            next_node = node_to_return.next
            self.head = next_node
            self.size -= 1
        return node_to_return.data

    def stack_size(self) ->  int:
        return self.size

    def print(self):
        print(self.head)
    


        
s = Stack()
s.print()

s.push(10)
s.print()        
s.push(20)
s.print()  
s.push(30)
s.print()  
print(s.stack_size())      

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 

print(s.pop())
s.print()  
print(s.stack_size()) 
