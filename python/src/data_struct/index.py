from binary_tree import Binary_tree, Node
from link_list import Complex_linklist, Complex_Node


def transform(tree):
    link = Complex_linklist()
    MFS(tree, link)
    return link


def MFS(tree, link):
    pointer = None

    def _MFS(node):
        nonlocal pointer

        if node.left != None:
            _MFS(node.left)
        if pointer != None:
            new_node = Complex_Node(node.data)
            new_node.prev = pointer
            pointer.next = new_node
            pointer = new_node
        else:
            link.head = Complex_Node(node.data)
            pointer = link.head
        if node.right != None:
            _MFS(node.right)

    _MFS(tree.root)


tree = Binary_tree()
tree.root = Node(10)
tree.root.left = Node(6)
tree.root.left.left = Node(4)
tree.root.left.right = Node(8)
tree.root.right = Node(14)
tree.root.right.left = Node(12)
tree.root.right.right = Node(16)


link_list = transform(tree)
result = []

pointer = link_list.head
while pointer != None:
    result.append(pointer.data)
    pointer = pointer.next

print(result)