# author : 'wangzhong';
# date: 03/12/2020 14:56

"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

思路：用三个字典去存储出现次数，左边，和右边
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for index, num in enumerate(nums):
            if num not in left:
                left[num] = index
            right[num] = index
            # 没有值时，返回0
            count[num] = count.get(num, 0) + 1
        max_value = max(count.values())
        ans = len(nums)
        for i in count:
            if count[i] == max_value:
                ans = min(ans, right[i] - left[i] + 1)
        return ans


if __name__ == '__main__':
    a = [1, 2, 2, 3, 1]
    ans = Solution().findShortestSubArray(a)
    print(ans)
