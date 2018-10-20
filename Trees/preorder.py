
    
#Iterative Preorder Traversal of Tree in O(n) time and space
def preorderTraversal(t):
    tree = []
    stack = []
    
    if t:
        stack.append(t)
    
    while stack:
        tmp = stack.pop()
        tree.append(tmp.value)
        
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
            
    return tree

def printOrder(t):
    
    preorder = preorderTraversal(t)       
    print(preorder)