# author : 'wangzhong';
# date: 04/01/2021 15:23

"""
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
"""

class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)
        if n < 2:
            return n
        temp, left, right = 0, 0, 1
        for i in range(2, n + 1):
            temp = left
            left = right
            right = temp + left
        return right