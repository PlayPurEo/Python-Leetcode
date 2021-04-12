# author : 'wangzhong';
# date: 07/01/2021 15:03

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                self.parent[root_x] = root_y

        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        ans = []
        count = 0
        for i in range(len(isConnected)):
            if uf.find(i) not in ans:
                ans.append(uf.find(i))
                count += 1
        return count