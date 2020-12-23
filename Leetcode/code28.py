# author : 'wangzhong';
# date: 22/12/2020 15:21

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        l = len(needle)
        pointer1 = 0
        while pointer1 < n - l + 1:

            while pointer1 < n - l + 1 and haystack[pointer1] != needle[0]:
                pointer1 += 1
            pointer2 = 0
            curLen = 0
            while pointer1 < n and pointer2 < l and haystack[pointer1] == needle[pointer2]:
                pointer2 += 1
                pointer1 += 1
                curLen += 1
            if curLen == l:
                return pointer1 - l
            else:
                # 下一个匹配位置
                pointer1 = pointer1 - curLen + 1
        return -1

        return -1