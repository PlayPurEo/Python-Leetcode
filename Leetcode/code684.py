# author : 'wangzhong';
# date: 13/01/2021 13:04

"""
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。
答案边 [u, v] 应满足相同的格式 u < v。
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        class unionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n + 1)]

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootY != rootX:
                    self.parent[rootX] = rootY
        n = len(edges)
        uf = unionFind(n)
        for x, y in edges:
            if uf.find(x) != uf.find(y):
                uf.union(x, y)
            else:
                return [x, y]
        return []