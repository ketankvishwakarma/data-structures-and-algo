from typing import Any


class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
    
    def __str__(self) -> str:
        return "{} --> {}".format(self.data,self.next)

class Queue:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self,data) -> bool:
        new_node = Node(data)
        if self.size==0:
            self.head = new_node
            self.tail = new_node
            self.size+=1
        else:
            tmp = self.tail
            self.tail = new_node
            tmp.next = new_node
            self.size+=1
        return True

    def dequeue(self) -> Any:
        if self.size ==0:
            return False
        else:
            new_head = self.head.next
            self.head = new_head
            self.size-=1
        return True
            
    def queue_lenght(self) -> int:
        return self.size


    def print(self):
        print("{} | {}".format(self.size,self.head))

q = Queue()

print(q.queue_lenght())
q.enqueue(10)
q.print()
q.enqueue(20)
q.print()
q.enqueue(30)
q.print()
q.enqueue(40)
q.print()
print(q.queue_lenght())
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()