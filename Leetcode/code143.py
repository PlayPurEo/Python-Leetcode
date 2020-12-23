# author : 'wangzhong';
# date: 09/12/2020 02:20

"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        s = []
        while head:
            s.append(head)
            head = head.next
        i = 1
        j = len(s) - 1
        cur = s[0]
        while i <= j:
            if i == j:
                cur.next = s[j]
                cur = cur.next
            else:
                cur.next = s[j]
                s[j].next = s[i]
                cur = s[i]
            i += 1
            j -= 1
        cur.next = None