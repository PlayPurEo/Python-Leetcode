# author : 'wangzhong';
# date: 24/11/2020 21:57

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

解法：动态规划
1.单个字符一定是回文
2.两个字符判断两个是否相等
3.多个字符判断两边是否相等和中间是否相等
"""
from typing import Tuple


class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s or len(s) == 1:
    #         return s
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     ans = ""
    #     # 字串的长度: l+1
    #     for l in range(0, n):
    #         # 字串起始位置
    #         for i in range(n):
    #             # 字串结束位置
    #             j = i + l
    #             if j >= len(s):
    #                 break
    #             if l == 0:
    #                 dp[i][j] = True
    #             elif l == 1:
    #                 dp[i][j] = s[i] == s[j]
    #             else:
    #                 dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
    #             if dp[i][j] and (l + 1) > len(ans):
    #                 ans = s[i:j + 1]
    #     return ans
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                start = i
        # 长度为l+1
        for l in range(2, n):
            # i + l < n
            for i in range(n - l):
                j = i + l
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                if dp[i][j]:
                    start = i
                    max_length = l + 1
        return s[start: start + max_length]


def expand(s: str, left: int, right: int) -> Tuple:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


# 中心拓展法， 效率比动态规划好
def zhongxintuozhan(s: str) -> str:
    if not s or len(s) == 1 or s == s[::-1]:
        return s
    n = len(s)
    end, start = 0, 0
    for i in range(n):
        left1, right1 = expand(s, i, i)
        left2, right2 = expand(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end + 1]


# 尾部标记法
def weibubiaoji(s: str) -> str:
    if not s:
        return ""
    if len(s) == 1 or s == s[::-1]:
        return s
    max_len, start = 1, 0
    # i就是当前的尾部，往前滑动考虑前面的所有大于max_len的情况，考虑奇偶性
    for i in range(1, len(s)):
        odd = s[i - max_len - 1: i + 1]
        even = s[i - max_len: i + 1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
            continue
    return s[start: start + max_len]


if __name__ == '__main__':
    s = 'abaabcbad'
    solution = Solution()
    ans = solution.longestPalindrome(s)
    print(ans)