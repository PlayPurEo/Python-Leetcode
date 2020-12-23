# author : 'wangzhong';
# date: 08/12/2020 19:53

"""
反转链表
解法：递归
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
