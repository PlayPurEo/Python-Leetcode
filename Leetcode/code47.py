# author : 'wangzhong';
# date: 25/12/2020 19:48

"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        check = [0 for _ in range(len(nums))]
        nums.sort()
        def helper(nums: List[int]):
            if len(temp) == len(nums):
                ans.append(list(temp))
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                temp.append(nums[i])
                check[i] = 1
                helper(nums)
                temp.pop()
                check[i] = 0
        helper(nums)
        return ans

if __name__ == '__main__':
    a = [1, 2, 3]
    print(a + 1)