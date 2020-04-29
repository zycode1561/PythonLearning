#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    p = ListNode(0)
    pre = p
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        pre.next = ListNode(s % 10)
        pre = pre.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if carry > 0:
        pre.next = ListNode(1)
    return p.next


node1 = ListNode(2)
node3 = ListNode(4)
node5 = ListNode(3)
node1.next = node3
node3.next = node5
node2 = ListNode(5)
node4 = ListNode(6)
node6 = ListNode(4)
node2.next = node4
node4.next = node6

res = addTwoNumbers(node1, node2)

while res:
    print(res.val, end=' ')
    res = res.next
