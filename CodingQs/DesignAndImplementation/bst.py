
class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, value) -> None:
        self.root = Node(value)

    def insert(self, value):
        node = Node(value)
        curr = self.root
        while curr:
            if value > curr.value:
                if curr.right == None:
                    curr.right = node
                    break
                else:
                    curr = curr.right
            elif value <= curr.value:
                if curr.left == None:
                    curr.left = node
                    break
                else:
                    curr = curr.left

        return self.root

    def lookup(self, value):
        curr = self.root
        while curr:
            if value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left
            else:
                return curr

        return curr

    # Balanced version
    def remove(self, value):
        # Find the node
        # Go right -> then go all the way down to the leftmost leaf node
        # Replace current node left leaf

        # Corner case where we remove root
        if value == self.root.value:
            left_tree = self.root.left
            right_tree = self.root.right
            self.root = self.root.right
            while self.root.left is not None:
                self.root = self.root.left

            self.root.left = left_tree
            self.root.right = right_tree
            return self.root
        
        lag = self.root
        if value > self.root.value:
            lead = self.root.right
            direction = 'r'
        else:
            lead = self.root.left
            direction = 'l'

        while lead:
            if value > lead.value:
                lag = lead
                lead = lead.right
            elif value < lead.value:
                lag = lead 
                lead = lead.left
            else:
                if not lead.left and not lead.right: # Leaf node
                    if direction == 'l':
                        lag.left = None
                    else:
                        lag.right = None
                    return self.root
                
                left_tree = lead.left
                right_tree = lead.right
                lead = lead.right
                self_looped = True
                while lead.left is not None:
                    self_looped = False
                    lead = lead.left
                
                if direction == 'l':
                    lag.left = lead
                else:
                    lag.right = lead
                lead.left = left_tree
                if self_looped:
                    lead.right = None
                else:
                    lead.right = right_tree
                
                return self.root

    def bfs(self):
        queue = [self.root]
        arr = []
        while queue:
            # print([s.value for s in stack])
            # print(arr)
            node = queue.pop(0)
            if node:
                arr.append(node.value)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return arr

    def bfsRecursive(self, queue, arr):
        if len(queue) == 0: 
            return arr

        current = queue.pop(0)
        arr.append(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        return self.bfsRecursive(queue, arr)

    def dfsInOrder(self, node, arr):
        # In order version
        if node.left is None and node.right is None:
            return arr.append(node.value)

        if node.left:
            self.dfsInOrder(node.left, arr)
        
        arr.append(node.value)

        if node.right:
            self.dfsInOrder(node.right, arr)
        
        return arr

    def dfsPreOrder(self, node, arr):
        if node.left is None and node.right is None:
            return arr.append(node.value)

        arr.append(node.value)
        if node.left:
            self.dfsPreOrder(node.left, arr)
        if node.right:
            self.dfsPreOrder(node.right, arr)

        return arr

    def dfsPostOrder(self, node, arr):
        if node.left is None and node.right is None:
            return arr.append(node.value)

        if node.left:
            self.dfsPostOrder(node.left, arr)
        if node.right:
            self.dfsPostOrder(node.right, arr)
        arr.append(node.value)
        
        return arr
        
tree = BST(9)
# print(tree.root.value)
tree.insert(4)
# print(tree.root.left.value)
tree.insert(6)
# print(tree.root.left.right.value)
tree.insert(20)
# print(tree.root.right.value)
tree.insert(170)
# print(tree.root.right.right.value)
tree.insert(15)
# print(tree.root.right.left.value)
tree.insert(1)
# print(tree.root.left.left.value)
# tree.insert(190)
# tree.insert(25)
# tree.insert(12)
# tree.insert(16)


# print(tree.lookup(20).right.value)
# print(tree.lookup(20).left.value)

# tree.remove(170)
print(tree.root.left.value)
print(tree.root.right.right.value)
print(tree.root.left.left.value)

# print(tree.bfs())
# print(tree.bfsRecursive([tree.root], []))
print(tree.dfsInOrder(tree.root, []))
print(tree.dfsPreOrder(tree.root, []))
print(tree.dfsPostOrder(tree.root, []))