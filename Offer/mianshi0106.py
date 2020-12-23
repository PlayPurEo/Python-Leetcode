# author : 'wangzhong';
# date: 23/12/2020 15:39

"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）
"""

import collections

class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        s = S[0]
        count = 1
        for i in range(1, len(S)):
            if S[i] != S[i - 1]:
                s += str(count)
                s += S[i]
                count = 1
            else:
                count += 1
        s += str(count)
        return len(s) < len(S) and s or S