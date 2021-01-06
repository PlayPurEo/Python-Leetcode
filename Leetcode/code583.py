# author : 'wangzhong';
# date: 23/12/2020 18:37

"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
解法：先找出最长公共字串的长度
步数 = len(word1) + len(word2) - 2*length
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2 or word1 == word2:
            return 0
        n1 = len(word1)
        n2 = len(word2)
        ans = [[0] * (n2 + 1)] * (n1 + 1)
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])
        print(ans)
        return n1 + n2 - 2 * ans[n1][n2]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1),len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp)
        return n+m-2*dp[n][m]

if __name__ == '__main__':
    print([1,2,3]*4)