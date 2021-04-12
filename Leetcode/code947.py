# author : 'wangzhong';
# date: 15/01/2021 16:47

"""
n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
"""
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 返回可以移除的石子的最大数量，同行或同列，可移除
        uf = UnionFind()
        for stone1, stone2 in stones:
            uf.union(stone1 + 10001, stone2)
        return len(stones) - uf.getCount()


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def getCount(self):
        return self.count

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = self.parent[root_y]
        self.count -= 1