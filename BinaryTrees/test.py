example = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]

def reconstruct_preorder(preorder):
    
    if not preorder:
        return None
	
	# Initialize stack and hashmap
    root = BinaryTreeNode(preorder[0])
    stack = [root]
    child_map = {root.data: 0}
    
    for i in range(1, len(preorder)):
        # Number of children found in latest node in stack
        top_count = child_map[stack[-1].data]
        if preorder[i]:
            new_node = BinaryTreeNode(preorder[i])
            if top_count == 0:
                stack[-1].left = new_node
                top_count = 1
            elif top_count == 1:
                stack[-1].right = new_node
                top_count += 1
                stack.pop()
			
            stack.append(new_node)
            child_map[new_node.data] = 0
        else:
            top_count += 1
            if top_count == 2:
                stack.pop()

    return root

tree = reconstruct_preorder(example)
tree_traversal_preorder(H)