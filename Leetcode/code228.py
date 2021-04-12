# author : 'wangzhong';
# date: 10/01/2021 14:01
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] < nums[i + 1] - 1:
                end = nums[i]
                if start == end:
                    ans.append(str(end))
                else:
                    ans.append(str(start) + "->" + str(end))
                if i < len(nums) - 1:
                    start = nums[i + 1]
        return ans