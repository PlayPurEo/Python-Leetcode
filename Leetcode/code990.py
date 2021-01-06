# author : 'wangzhong';
# date: 06/01/2021 14:45

"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false
"""
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def find(self, x):
                while x != self.parent[x]:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                self.parent[root_x] = root_y

            def is_connected(self, x, y):
                return self.find(x) == self.find(y)

        unionFind = UnionFind(26)
        for equation in equations:
            if equation[1] == '=':
                index1 = ord(equation[0]) - ord('a')
                index2 = ord(equation[3]) - ord('a')
                unionFind.union(index1, index2)

        for equation in equations:
            if equation[1] == '!':
                index1 = ord(equation[0]) - ord('a')
                index2 = ord(equation[3]) - ord('a')
                if unionFind.is_connected(index1, index2):
                    return False
        return True
