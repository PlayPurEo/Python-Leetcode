# author : 'wangzhong';
# date: 09/12/2020 00:44

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

解法：数学归纳和动态规划
"""
from scipy.special import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m为列，n为行
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        cur = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                cur[j] = cur[j] + cur[j - 1]
        return cur[-1]
    # 排列组合
    def uniquePaths2(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)


if __name__ == '__main__':
    print(Solution().uniquePaths2(7, 3))