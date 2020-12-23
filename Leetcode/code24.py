# author : 'wangzhong';
# date: 26/11/2020 14:34

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from Leetcode.code02 import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        这里只是交换了数值，并没有进行内存的交换
        :param head:
        :return:
        """
        if not head:
            return head
        nodeIndex = 0
        temp = head
        while head is not None and head.next is not None:
            if nodeIndex % 2 == 0:
                head.val, head.next.val = head.next.val, head.val
            nodeIndex += 1
            head = head.next
        return temp

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs2(newHead.next)
        newHead.next = head
        return newHead

if __name__ == '__main__':
    root = ListNode(1)
    next1 = ListNode(2)
    next2 = ListNode(3)
    root.next = next1
    next1.next = next2
    head = Solution().swapPairs2(root)
    while head is not None:
        print(head.val)
        head = head.next