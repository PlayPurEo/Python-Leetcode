# author : 'wangzhong';
# date: 08/12/2020 20:00

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        s.reverse()
        return s


    def reversePrint2(self, head: ListNode, s: List) -> List[int]:
        if not head:
            return
        self.reversePrint2(head.next, s)
        s.append(head.val)
        return s


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    s = []
    print(Solution().reversePrint2(a, s))