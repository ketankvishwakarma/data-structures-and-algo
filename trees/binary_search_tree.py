class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        
        node = Node(value=value)
        # if tree is empty
        if self.root == None:
            self.root = node
            return self

        # if tree has nodes, treverse tree util currect position is found
        current = self.root
        while True:
            # we have duplicate value, discard it
            if value == current.value: return self

            # if value is smaller look into left side if the tree
            if value < current.value:
                if current.left == None:
                    current.left = node
                    return self
                else:
                    current = current.left
            # if value is greater, look into right side if the tree
            elif value > current.value:
                if current.right == None:
                    current.right = node
                    return self
                else:
                    current = current.right
    
    def find(self, value) -> bool:
        if self.root == None:
            return False
        
        current = self.root
        while True:
            if value == current.value: return True
            if value < current.value:
                if current.left == None: return False
                else: current = current.left
            else:
                if current.right == None: return False
                else: current = current.right


            




    def print_tree(self,node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            print(' ' * 6 * level + '->', node.value)
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
s.print_tree(s.root)
print("search for 10 results in {}".format(s.find(10)))
print("search for 2 results in {}".format(s.find(2)))
print("search for 20 results in {}".format(s.find(20)))


