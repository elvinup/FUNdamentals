import collections

def postorderTraversal(t):    
    stack1 = []
    stack2 = collections.deque()
    
    if t:
        stack2.appendleft(t.value)
        if t.left:
            stack1.append(t.left)
        if t.right:
            stack1.append(t.right)
    
    while stack1:
        
        tmp = stack1.pop()
        stack2.appendleft(tmp.value)
        
        if tmp.left:
            stack1.append(tmp.left)
        if tmp.right:
            stack1.append(tmp.right)
        
    
    return list(stack2)

def printOrder(t):

    postorder = postorderTraversal(t)
    print(postorder)