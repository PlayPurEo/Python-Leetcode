# author : 'wangzhong';
# date: 08/12/2020 17:53

"""
用一个 非空 单链表表示一个非负整数，将这个整数加一。

你可以假设这个整数除了 0 本身，没有任何前导 0 。

这个整数的各个数位按照高位在链表头，低位在链表尾的顺序排列。

解法： 递归从末位开始加一
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def plusOne(self, head: ListNode) -> ListNode:
        num = self.sumNode(head)
        if num:
            final = ListNode(1)
            final.next = head
            head = final
        return head

    def sumNode(self, head: ListNode) -> int:
        num = head.next and self.sumNode(head.next) or 1
        head.val += num
        num = head.val // 10
        head.val %= 10
        return num
