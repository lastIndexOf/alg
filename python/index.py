class Node:
    left = None
    right = None

    def __init__(self, data=''):
        self.data = data


class BinaryTree:
    root = None


def rebuildTree(front=[], middle=[]):
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
            front[index+1:len(front)], middle[index+1:len(middle)])

        return node

    tree = BinaryTree()
    tree.root = _rebuild(front, middle)

    return tree

result = []
def FFS(node):
    result.append(node.data)
    if node.left != None:
        FFS(node.left)
    if node.right != None:
        FFS(node.right) 

if __name__ == '__main__':
    frontTravel = [1, 2, 4, 7, 3, 5, 6, 8]
    middleTravel = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = rebuildTree(frontTravel, middleTravel)
    FFS(tree.root)
    print(result)