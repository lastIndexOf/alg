"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = None
        root = None

        rest = 0
        while l1 != None or l2 != None or rest != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            result = int((l1_value + l2_value + rest) % 10)
            rest = int((l1_value + l2_value + rest - result) / 10)

            if new_list:
                new_list.next = ListNode(result)
                new_list = new_list.next
            else:
                new_list = ListNode(result)
                root = new_list

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return root


s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ret = s.addTwoNumbers(l1, l2)
