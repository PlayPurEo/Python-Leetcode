# author : 'wangzhong';
# date: 22/12/2020 14:17

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        leftToRight = True
        while queue:
            n = len(queue)
            content = []
            for i in range(n):
                node = queue.popleft()
                if leftToRight:
                    content.append(node.val)
                else:
                    content.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            leftToRight = not leftToRight
            ans.append(content)
        return ans