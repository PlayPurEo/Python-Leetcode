# author : 'wangzhong';
# date: 07/01/2021 16:23

"""
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            n = len(queue)
            content = []
            for i in range(n):
                node = queue.popleft()
                content.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.insert(0, content)
        return ans