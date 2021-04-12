# author : 'wangzhong';
# date: 19/01/2021 12:52

"""
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接
"""
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class unionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))

            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y) -> bool:
                rootX = self.find(x)
                rootY = self.find(y)
                if rootY == rootX:
                    return False
                self.parent[rootX] = rootY
                return True
        n = len(points)
        uf = unionFind(n)
        edges = list()
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        edges.sort()

        res = 0
        num = 1
        for length, x, y in edges:
            if uf.union(x, y):
                res += length
                num += 1
                if num == n:
                    break
        return res