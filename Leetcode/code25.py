# author : 'wangzhong';
# date: 23/12/2020 14:42

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        stack = []
        cur = fakehead = ListNode()
        count = k
        while head:
            while head and count:
                stack.append(head)
                head = head.next
                count -= 1
            if not count:
                while stack:
                    cur.next = stack.pop()
                    cur = cur.next
            if not head:
                while stack:
                    cur.next = stack.pop(0)
                    cur = cur.next
            count = k
            cur.next = None
        return fakehead.next