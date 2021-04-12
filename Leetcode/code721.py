# author : 'wangzhong';
# date: 18/01/2021 15:41

"""
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。
一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。
"""
import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        class unionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    self.parent[rootX] = rootY

        emailToIndex = dict()
        emailToName = dict()
        emailIndex = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = emailIndex
                    emailIndex += 1
                    emailToName[email] = name
        uf = unionFind(emailIndex)
        # 邮箱进行合并
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                secondIndex = emailToIndex[email]
                uf.union(firstIndex, secondIndex)
        res = collections.defaultdict(list)
        for email in emailToIndex.keys():
            rootIndex = uf.find(emailToIndex[email])
            res[rootIndex].append(email)
        ans = []
        for emails in res.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans