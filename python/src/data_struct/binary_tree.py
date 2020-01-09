class Node:
    left = None
    right = None

    def __init__(self, data=''):
        self.data = data


class Binary_tree:
    root = None


def rebuild_tree(front=[], middle=[]):

    def _rebuild(front=[], middle=[]):
        if (len(front) == 0 or len(middle) == 0 or len(front) != len(middle)):
            return None
        root = front[0]
        node = Node(root)

        index = 0
        while middle[index] != root:
            index = index + 1

        node.left = _rebuild(front[1:index+1], middle[0:index])
        node.right = _rebuild(
            front[index+1:len(front)], middle[index+1:len(middle)]
        )

        return node

    tree = Binary_tree()
    tree.root = _rebuild(front, middle)

    return tree


result = []


def FFS(node):
    result.append(node.data)
    if node.left != None:
        FFS(node.left)
    if node.right != None:
        FFS(node.right)


def calc_path(tree=Binary_tree(), target=0):
    if tree.root == None:
        return []

    res = []
    path = []

    def _calc(node, target):
        nonlocal path
        nonlocal res

        path.append(node.data)
        rest = target - node.data

        if rest == 0:
            res.append([*path])
            path.pop()
            return

        if rest < 0:
            path.pop()
            return

        if node.left:
            _calc(node.left, rest)
        if node.right:
            _calc(node.right, rest)

        path.pop()

    _calc(tree.root, target)
    
    return res


if __name__ == '__main__':
    frontTravel = [1, 2, 4, 3, 3, 5, 6, 8]
    middleTravel = [4, 3, 2, 1, 5, 3, 8, 6]
    tree = rebuild_tree(frontTravel, middleTravel)
    # 前序遍历
    FFS(tree.root)
    print(calc_path(tree, 10))
    # 计算路径
