# author : 'wangzhong';
# date: 23/01/2021 14:45

"""

用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。
线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。
请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        for x, y in connections:
            uf.unite(x, y)

        return uf.setCount - 1
