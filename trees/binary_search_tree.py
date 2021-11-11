class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return self

        current = self.root
        while True:
            if value == current.value : return self.root
            if value > current.value:
                if current.right == None:
                    current.right = node
                    return self.root
                else:
                    current = current.right
            elif value < current.value:
                if current.left == None:
                    current.left = node
                    return self.root
                else:
                    current = current.left
    
    def print_tree(self,node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

s = BST()
s.insert(10)
s.insert(5)
s.insert(13)
s.insert(7)
s.insert(2)
s.insert(11)
s.insert(13)
s.insert(16)
s.insert(1)
s.insert(9)
s.insert(3)

s.print_tree(s.root)