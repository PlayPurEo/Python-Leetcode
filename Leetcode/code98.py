# author : 'wangzhong';
# date: 14/12/2020 23:21

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root)
