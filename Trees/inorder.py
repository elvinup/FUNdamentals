#Iterative Inorder Traversal of Tree in O(n) time and space
def inorderTraversal(t):
    tree = []
    stack = []
    
    curr = t
    
    while True:
        
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if stack:
                curr = stack.pop()
                tree.append(curr.value)
                curr = curr.right
            else:
                break
    return tree

def printOrder(t):

    inorder = inorderTraversal(t)
    print(inorder)
