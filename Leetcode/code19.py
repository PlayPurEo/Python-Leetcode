# author : 'wangzhong';
# date: 09/12/2020 00:12

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = head
        after = ListNode(-1)
        after.next = head
        head = after
        for i in range(n):
            prev = prev.next
        while prev:
            prev = prev.next
            after = after.next
        after.next = after.next.next
        return head.next
