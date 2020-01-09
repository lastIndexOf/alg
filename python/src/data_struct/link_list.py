class Complex_Node:
    next = None
    prev = None
    sibling = None

    def __init__(self, data=''):
        self.data = data


class Complex_linklist:
    head = None

    def add(self, data):
        node = ComplexNode(data)

        if self.head == None:
            self.head = node
            return node

        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next

        pointer.next = node
        return node


def clone_Complex(linklist):
    new_list = Complex_linklist()

    if linklist.head == None:
        return new_list

    new_list.head = Complex_Node(linklist.head.data)
    new_pointer = new_list.head
    old_pointer = linklist.head

    hash = dict({old_pointer: new_pointer})
    while old_pointer.next != None:
        new_pointer.next = Complex_Node(old_pointer.next.data)
        new_pointer = new_pointer.next
        old_pointer = old_pointer.next
        hash[old_pointer] = new_pointer

    old_pointer = linklist.head
    new_pointer = new_list.head

    while old_pointer != None:
        new_pointer.sibling = hash.get(
            old_pointer) if hash.get(old_pointer) != None else None
        new_pointer = new_pointer.next
        old_pointer = old_pointer.next

    return new_pointer
