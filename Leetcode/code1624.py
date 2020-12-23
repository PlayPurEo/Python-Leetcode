# author : 'wangzhong';
# date: 22/12/2020 17:00

"""
给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。

子字符串 是字符串中的一个连续字符序列。
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        res = -1
        for ids, ch in enumerate(s):
            if ch in d:
                res = max(res, ids - d[ch] - 1)
            else:
                d[ch] = ids
        return res