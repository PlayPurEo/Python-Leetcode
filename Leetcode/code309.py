# author : 'wangzhong';
# date: 21/12/2020 14:14

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, -prices[0]]]
        sell = max(dp[0][0], dp[0][1] + prices[1])
        buy = max(dp[0][1], dp[0][0] - prices[1])
        dp.append([sell, buy])
        for i in range(2, len(prices)):
            sell = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            buy = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            dp.append([sell, buy])
        return dp[-1][0]
