# author : 'wangzhong';
# date: 21/12/2020 13:45

"""
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        ans = [0, 0]
        for i in range(2, len(cost) + 1):
            ans.append(min(cost[i - 2] + ans[i - 2], cost[i - 1] + ans[i - 1]))
        return ans[-1]