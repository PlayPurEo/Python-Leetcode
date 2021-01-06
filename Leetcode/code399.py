# author : 'wangzhong';
# date: 06/01/2021 12:08

"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
解法：并查集
"""
from typing import List


class unionFind:
    def __init__(self):
        self.father = {}
        self.weight = {}

    def find(self, x: str):
        if x != self.father[x]:
            origin = self.father[x]
            self.father[x] = self.find(origin)
            self.weight[x] *= self.weight[origin]
        return self.father[x]

    def add(self, x: str):
        if x not in self.father:
            self.father[x] = x
            self.weight[x] = 1.0

    def merge(self, x: str, y: str, val: float):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.father[rootX] = rootY
            self.weight[rootX] = val * self.weight[y] / self.weight[x]

    def isConnected(self, x: str, y: str):
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = unionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)
        res = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.isConnected(a, b):
                res[i] = uf.weight[a] / uf.weight[b]
        return res

if __name__ == '__main__':
    res = [[0] for _ in range(10)]
    res[0][0] = 9
    print(res)