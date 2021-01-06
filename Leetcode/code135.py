# author : 'wangzhong';
# date: 24/12/2020 13:10

"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

解法：两次遍历，左遍历和右遍历，找出每个孩子的最大分糖值
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans1 = [1 for _ in range(len(ratings))]
        ans2 = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ans1[i] = ans1[i - 1] + 1
        count = ans1[-1]
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                ans2[i - 1] = ans2[i] + 1
            count += max(ans1[i - 1], ans2[i - 1])
        return count