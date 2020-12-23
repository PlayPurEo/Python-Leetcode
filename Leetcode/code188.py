# author : 'wangzhong';
# date: 21/12/2020 23:17

"""
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k < 1:
            return 0
        n = len(prices)
        if k >= n // 2:
            maxProfit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    maxProfit += prices[i] - prices[i - 1]
            return maxProfit

        dp = [[[0, float('-inf')] for _ in range(k + 1)]] * n
        dp[0][0] = [0, 0]
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        lastDp = dp[k]
        maxProfit = 0
        for i in range(1, k + 1):
            if lastDp[i][0] > maxProfit:
                maxProfit = lastDp[i][0]
        return maxProfit



if __name__ == '__main__':
    dp = [[1] for _ in range(19)]
    print(dp)