# author : 'wangzhong';
# date: 08/12/2020 19:45

"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(-1)
        temp1 = small
        big = ListNode(-1)
        temp2 = big
        while head:
            if head.val < x:
                temp1.next = head
                temp1 = temp1.next
                head = head.next
            else:
                temp2.next = head
                temp2 = temp2.next
                head = head.next
        temp2.next = None
        temp1.next = big.next
        return small.next