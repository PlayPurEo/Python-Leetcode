# author : 'wangzhong';
# date: 05/01/2021 15:31

"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1