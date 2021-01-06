# author : 'wangzhong';
# date: 23/12/2020 17:28

"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

    def addStrings2(self, num1: str, num2: str) -> str:
        m, n = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        while m >=0 or n>= 0:
            n1 = int(num1[m]) if m >= 0 else 0
            n2 = int(num2[n]) if n >= 0 else 0
            temp = n1 + n2 + carry
            carry = temp // 10
            res = str(temp % 10) + res
            m -= 1
            n -= 1
        return "1" + res if carry > 0 else res