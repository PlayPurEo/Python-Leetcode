# author : 'wangzhong';
# date: 17/12/2020 14:21

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

解法：动态规划

1. 定义状态转移方程
定义二维数组 dp[n][2]：

dp[i][0] 表示第 i 天不持有可获得的最大利润；
dp[i][1] 表示第 i 天持有可获得的最大利润（注意是第 i 天持有，而不是第 i 天买入）


定义状态转移方程：
不持有：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
对于今天不持有，可以从两个状态转移过来：1. 昨天也不持有；2. 昨天持有，今天卖出。两者取较大值。

持有：dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
对于今天持有，可以从两个状态转移过来：1. 昨天也持有；2. 昨天不持有，今天买入。两者取较大值。

优化：今天的值只会从昨天而来，所以第一维可以直接去掉
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0, -prices[0]]
        for i in range(1, len(prices)):
            temp = dp[0]
            dp[0] = max(temp, dp[1] + prices[i] - fee)
            dp[1] = max(temp - prices[i], dp[1])
        return dp[0]