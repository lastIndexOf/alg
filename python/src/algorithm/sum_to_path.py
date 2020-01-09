def to_path(tree, target):
    ret = []
    root = tree.root
    path = []
    path_sum = 0

    def ffs(node, path):
        if node == None:
            return

        if not handle_node(node, path):
            return

        if node.left:
            ffs(node.left)
        if node.right:
            ffs(node.right)
        
        path.pop()

    def handle_node(node, path):
        path_sum += node.data
        if path_sum == target:
            path.append(node.data)
            ret.append([*path])
            path.pop()
            return False
        elif path_sum > target:
            return False
        else:
            path.append(node.data)
            return True

    ffs(root, path)

    return ret
