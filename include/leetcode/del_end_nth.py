#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

from commons.listnode import *


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    pre = ListNode(-1)
    pre.next = head
    fir, sec = head, head
    while n > 1:
        sec = sec.next
        n -= 1
    if not sec.next:
        return head.next
    while sec.next:
        sec = sec.next
        fir = fir.next
        pre = pre.next
    pre.next = pre.next.next
    return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

removeNthFromEnd(l1, 2)

while l1:
    print(l1.val, end=" ")
    l1 = l1.next
print()
