# author : 'wangzhong';
# date: 06/12/2020 22:07

"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 自己想的，性能极差
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        firstNode = lists[0]
        fakeNode = ListNode(val=-999999, next=firstNode)
        for i in range(1, len(lists)):
            target = lists[i]
            firstNode = fakeNode
            while firstNode and target:
                if firstNode.val <= target.val and firstNode.next and firstNode.next.val <= target.val:
                    firstNode = firstNode.next
                else:
                    temp = target
                    target = target.next
                    temp.next = firstNode.next
                    firstNode.next = temp
                    firstNode = firstNode.next
        return fakeNode.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    a = ListNode(6)
    b = ListNode(5, a)
    c = ListNode(4, b)
    d = ListNode(3)
    e = ListNode(2, d)
    f = ListNode(1, e)
    finalNode = Solution().mergeKLists([c, f])
