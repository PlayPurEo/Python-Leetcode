# author : 'wangzhong';
# date: 18/12/2020 14:41

"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

说明：java可以直接用字符数组去储存出现次数，因为字符可以直接做加减，python只能用字典
解法一：统计次数，python直接用collection counter
解法二：异或
"""
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(collections.Counter(t) - collections.Counter(s))[0]