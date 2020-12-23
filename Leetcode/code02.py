# author : 'wangzhong';
# date: 24/11/2020 14:24

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # 创建一个初始节点
        res = pre = ListNode(0)
        while l1 or l2 or carry:
            # 判断l1是否有值
            if l1: l1, carry = l1.next, l1.val + carry

            # 判断l2是否有值
            if l2: l2, carry = l2.next, l2.val + carry

            # 如果carry有值，说明需要增加节点
            carry, val = divmod(carry, 10)
            # 链式赋值，执行顺序为：pre.next = ListNode(val); pre = ListNode(val)
            pre.next = pre = ListNode(val)
        return res.next


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2, a)
    c = ListNode(1, b)
    d = ListNode(8)
    e = ListNode(7, d)
    f = ListNode(6, e)
    solution = Solution()
    res = solution.addTwoNumbers(c, f)
    list1 = []
    while res:
        list1.append(res.val)
        list1.append("->")
        res = res.next
    print(list1)
