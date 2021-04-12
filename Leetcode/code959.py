# author : 'wangzhong';
# date: 25/01/2021 00:03

"""
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。
这些字符会将方块划分为一些共边的区域。
（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。
"""
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        class unionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.count = n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    self.parent[rootX] = rootY
                    self.count -= 1

        n = len(grid)
        size = 4*n**2
        uf = unionFind(size)
        for i in range(n):
            s = grid[i]
            for j in range(n):
                index = 4 * n * i + 4 * j
                if s[j] == "/":
                    uf.union(index, index+3)
                    uf.union(index+1, index+2)
                elif s[j] == "\\":
                    uf.union(index, index+1)
                    uf.union(index+2, index+3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                if j + 1 < n:
                    uf.union(index + 1, 4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    uf.union(index + 2, 4 * ((i+1) * n + j))
        return uf.count