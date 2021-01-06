# author : 'wangzhong';
# date: 27/12/2020 23:32

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = {}
        for i in range(len(s)):
            if s[i] in pairs and pairs[s[i]] != t[i]:
                return False
            if s[i] not in pairs and t[i] in pairs.values():
                return False
            pairs[s[i]] = t[i]
        return True