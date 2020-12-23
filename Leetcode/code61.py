# author : 'wangzhong';
# date: 08/12/2020 17:24

"""

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        last = head
        prev = head
        n = 1
        while last.next:
            last = last.next
            n += 1
        last.next = head
        param = k % n
        length = n - param
        for i in range(0, length):
            prev = prev.next
            last = last.next
        last.next = None
        return prev