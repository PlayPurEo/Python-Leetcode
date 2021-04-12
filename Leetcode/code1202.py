# author : 'wangzhong';
# date: 11/01/2021 16:49

"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
"""
import collections
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class unionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def find(self, x):
                if self.parent[x] == x:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    self.parent[rootX] = rootY

        n = len(s)
        uf = unionFind(n)
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            uf.union(a, b)
        dic = collections.defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            dic[root].append(i)
        ans = list(s)
        for v in dic.values():
            # 属于一个通道的索引
            arr = [s[i] for i in v]
            arr.sort()
            for i in range(len(v)):
                ans[v[i]] = arr[i]
        return "".join(ans)


if __name__ == '__main__':
    s = "udyyek"
    pairs = [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]
    solution = Solution()
    solution.smallestStringWithSwaps(s, pairs)