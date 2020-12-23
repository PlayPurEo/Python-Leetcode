# author : 'wangzhong';
# date: 22/12/2020 16:39

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""

class Solution:
    def reverse(self, x):
        reverseNumber = 0
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        while x != 0:
            reverseNumber = reverseNumber * 10 + x % 10
            x = x // 10
            if sign * reverseNumber <= MIN or sign * reverseNumber >= MAX:
                return 0
        return sign * reverseNumber