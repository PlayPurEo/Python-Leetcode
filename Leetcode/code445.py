# author : 'wangzhong';
# date: 08/12/2020 18:46

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

解法：逆序就要用栈
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        ans = None
        while s1 or s2 or carry != 0:
            a = s1 and s1.pop() or 0
            b = s2 and s2.pop() or 0
            count = a + b + carry
            carry = count // 10
            num = count % 10
            head = ListNode(num)
            head.next = ans
            ans = head
        return ans
