# author : 'wangzhong';
# date: 17/12/2020 13:44

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
解法1：横向比较，即每一个单词依次比较
解法2：纵向比较，即所有单词从第一个字符开始比较
解法3：排序，然后直接比较头尾
"""
from typing import List


class Solution:
    # 横向比较
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            minLength = min(len(prefix), len(strs[i]))
            index = 0
            while index < minLength and prefix[index] == strs[i][index]:
                index += 1
            prefix = prefix[:index]
        return prefix

    # 纵向比较
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        for row in list(zip(*strs)):
            if len(set(row)) == 1:
                ans += row[0]
            else:
                break
        return ans

    # 排序后比较
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        minLength = min(len(first), len(last))
        index = 0
        while index < minLength and first[index] == last[index]:
            index += 1
        return first[:index]