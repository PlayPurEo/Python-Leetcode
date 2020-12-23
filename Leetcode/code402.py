# author : 'wangzhong';
# date: 20/12/2020 15:31

"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        length = len(num) - k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        return "".join(stack[:length]).lstrip('0') or '0'
