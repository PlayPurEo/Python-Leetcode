# author : 'wangzhong';
# date: 22/12/2020 23:45

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

解法：双指针滑动窗口
i = 0，j从0开始慢慢滑，直到包含t，然后移动i，把不必要的元素移除，计算长度
然后i再加一，j再移动，计算下一个包含t的长度
需要一个hashMap统计每个字符还需要的次数
需要一个count计算所有字符还需要的次数（否则每次都要统计hashmap里所有值的和是否等于0）
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        hashMap = collections.Counter(t)
        need = len(t)
        res = [0, len(s) + 1]
        for j, ch in enumerate(s):
            if ch in hashMap:
                # 如果是t中的字符，统计次数要减一，如果减完还是大于等于0，说明是需要的字符，need要减一，小于0说明需要字符的个数已经超了，need不用减
                hashMap[ch] -= 1
                if hashMap[ch] >= 0:
                    need -= 1
            if need == 0:
                # 移动i，不是需要字符的+1，或者是需要字符超过次数的也要+1，但这种情况，滑动后记得把次数加回来
                while s[i] not in hashMap or hashMap[s[i]] < 0:
                    if s[i] in hashMap:
                        hashMap[s[i]] += 1
                    i += 1
                # i移动完之后计算长度
                if j - i < res[1] - res[0]:
                    res[0], res[1] = i, j
                # 再移动一位，计算下个长度，把统计次数加回来
                hashMap[s[i]] += 1
                i += 1
                need += 1
        return res[1] < len(s) and s[res[0]:res[1] + 1] or ""

