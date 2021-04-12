# author : 'wangzhong';
# date: 16/01/2021 16:15

"""
有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。
每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。
一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

思路：并查集，敲碎砖块，逆序补上砖块进行合并，算出合并之后连上的砖块，就是敲碎会掉的砖块
"""
from typing import List


class Solution:
    DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def getIndex(self, x, y, col):
        return x * col + y

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        def inArea(x, y):
            return 0 <= x < row and 0 <= y < col

        class UnionFind():
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1 for _ in range(n)]

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootY != rootX:
                    self.parent[rootX] = rootY
                    self.size[rootY] += self.size[rootX]

            def getSize(self, x):
                rootX = self.find(x)
                return self.size[rootX]

        for x, y in hits:
            grid[x][y] -= 1
        row = len(grid)
        col = len(grid[0])
        size = row * col
        uf = UnionFind(size + 1)
        for j in range(col):
            if grid[0][j] == 1:
                uf.union(j, size)
        for i in range(1, row):
            for j in range(col):
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 1:
                        uf.union(self.getIndex(i, j, col), self.getIndex(i - 1, j, col))

                    if j > 0 and grid[i][j - 1] == 1:
                        uf.union(self.getIndex(i, j, col), self.getIndex(i, j - 1, col))
        hitLen = len(hits)
        res = [0 for _ in range(hitLen)]
        for i in range(hitLen - 1, -1, -1):
            x = hits[i][0]
            y = hits[i][1]
            grid[x][y] += 1
            if grid[x][y] == 0:
                continue
            origin = uf.getSize(size)
            if x == 0:
                uf.union(y, size)
            for addX, addY in self.DIRECTION:
                newX = x + addX
                newY = y + addY
                if inArea(newX, newY) and grid[newX][newY] == 1:
                    uf.union(self.getIndex(x, y, col), self.getIndex(newX, newY, col))

            current = uf.getSize(size)

            res[i] = max(0, current - origin - 1)
        return res


if __name__ == '__main__':
    res = []
    res.insert(0, 0)
    res.insert(0, 0)
    print(res)