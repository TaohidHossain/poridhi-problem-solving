class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    

arr = [1, 2, 3, 4, 5]
root = TreeNode(arr[0])
i = 1
queue = [root]

for node in queue:
    if i < len(arr):
        node.left = TreeNode(arr[i])
        queue.append(node.left)
        i += 1
    if i < len(arr):
        node.right = TreeNode(arr[i])
        queue.append(node.right)
        i += 1

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)
    

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')

def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print('\n')
        

print(root.value)
inorder_traversal(root)
print('\n')
preorder_traversal(root)
print('\n')
postorder_traversal(root)
print('\n')
level_order_traversal(root)