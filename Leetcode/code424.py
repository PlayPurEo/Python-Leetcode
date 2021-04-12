# author : 'wangzhong';
# date: 02/02/2021 21:02

"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left