# author : 'wangzhong';
# date: 23/12/2020 13:52

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for ids, ch in enumerate(s):
            if ch not in ans:
                ans[ch] = ids
            else:
                ans[ch] = -1
        for i in ans:
            if ans[i] >= 0:
                return ans[i]
        return -1