# author : 'wangzhong';
# date: 09/12/2020 01:41

"""
对链表进行插入排序。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = ListNode(0)
        first.next = head
        lastSort = head
        cur = head.next
        while cur:
            if cur.val >= lastSort.val:
                lastSort = lastSort.next
            else:
                prev = first
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSort.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSort.next
        return first.next
