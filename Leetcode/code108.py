# author : 'wangzhong';
# date: 24/12/2020 15:

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid + 1:]
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root