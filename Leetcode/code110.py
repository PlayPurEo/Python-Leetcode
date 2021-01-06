# author : 'wangzhong';
# date: 24/12/2020 16:

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 自顶向下
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root: TreeNode):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        if not root:
            return True
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    # 自底向下
    def isBalanced2(self, root: TreeNode) -> bool:
        def depthAndjudge(root):
            if not root:
                return 0
            left = depthAndjudge(root.left)
            if left == -1:
                return -1
            right = depthAndjudge(root.right)
            if right == -1:
                return -1
            return 1 + max(left, right) if abs(left - right) < 2 else -1
        return depthAndjudge(root) != -1