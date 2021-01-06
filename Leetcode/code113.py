# author : 'wangzhong';
# date: 24/12/2020 17:40

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans, temp = [], []

        def helper(root: TreeNode, sum: int, temp: List[int]):
            if not root:
                return
            temp.append(root.val)
            sum = sum - root.val
            if sum == 0 and not root.left and not root.right:
                ans.append(list(temp))
                temp.pop()
                return
            helper(root.left, sum, temp)
            helper(root.right, sum, temp)
            temp.pop()
        helper(root, sum, temp)
        return ans


if __name__ == '__main__':
    root = TreeNode(5)
    temp = []
    ans = []
    print(Solution().pathSum(root, 5))