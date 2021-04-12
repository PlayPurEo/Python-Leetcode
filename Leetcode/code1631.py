# author : 'wangzhong';
# date: 19/01/2021 13:33

"""
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，
其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。
"""
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class unionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))

            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootY != rootX:
                    self.parent[rootX] = rootY

        def valid(x, y):
            return 0 <= x < row and 0 <= y < col

        row = len(heights)
        col = len(heights[0])
        uf = unionFind(row * col)
        edges = list()
        for i in range(row):
            for j in range(col):
                rightx = i
                righty = j + 1
                if valid(rightx, righty):
                    edges.append((abs(heights[i][j] - heights[rightx][righty]), i*col + j, rightx*col + righty))
                downx = i + 1
                downy = j
                if valid(downx, downy):
                    edges.append((abs(heights[i][j] - heights[downx][downy]), i*col + j, downx*col + downy))
        edges.sort()
        res = 0
        for length, x, y in edges:
            if uf.find(0) == uf.find(row*col - 1):
                break
            uf.union(x, y)
            res = max(res, length)
        return res