# author : 'wangzhong';
# date: 06/02/2021 17:36

"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

回溯算法会超时
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        if not k:
            return 0
        length = len(cardPoints) - k
        preSum = 0
        for i in range(length):
            preSum += cardPoints[i]
        total = preSum
        for i in range(length, len(cardPoints)):
            preSum -= cardPoints[i - length]
            preSum += cardPoints[i]
            total = min(preSum, total)
        return sum(cardPoints) - total