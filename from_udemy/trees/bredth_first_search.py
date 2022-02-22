
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
            print("matching {} to {}".format(value,current.value))
            if value == current.value: return True
            if value < current.value:
                if current.left == None: return False
                else: current = current.left
            else:
                if current.right == None: return False
                else: current = current.right


    def bfs(self) -> list:
        queue = []
        visited = []
        if self.root == None: return visited
        queue.append(self.root)
        while len(queue)>0:
            first = queue.pop(0)
            visited.append(first.value)
            if first.left!=None:
                queue.append(first.left)
            if first.right!=None:
                queue.append(first.right) 
        return visited   

    def treverse_pre(self,node,visited)->list:
        visited.append(node.value)
        if node.left !=None: self.treverse_pre(node.left,visited)
        if node.right !=None: self.treverse_pre(node.right,visited)
        return visited

    def treverse_post(self,node,visited)->list:
        if node.left !=None: self.treverse_post(node.left,visited)
        if node.right !=None: self.treverse_post(node.right,visited)
        visited.append(node.value)
        return visited

    def treverse_in(self,node,visited)->list:
        if node.left !=None: self.treverse_in(node.left,visited)
        visited.append(node.value)
        if node.right !=None: self.treverse_in(node.right,visited)
        return visited

    def dfs_preorder(self)-> list:
        visited = []
        if self.root == None: return visited
        return self.treverse_pre(self.root,visited)

    def dfs_postorder(self)-> list:
        visited = []
        if self.root == None: return visited
        return self.treverse_post(self.root,visited)

    def dfs_inorder(self)-> list:
        visited = []
        if self.root == None: return visited
        return self.treverse_in(self.root,visited)


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

print("bfs      --> {}".format(s.bfs()))
print("dfs_pre  --> {}".format(s.dfs_preorder()))
print("dfs_post --> {}".format(s.dfs_postorder()))
print("dfs_in   --> {}".format(s.dfs_inorder()))

