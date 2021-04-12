# author : 'wangzhong';
# date: 20/01/2021 13:22

"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
解法：找出最大的三个数，最小的两个数
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        for num in nums:
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
        return max(max3*max2*max1, min2*min1*max1)


if __name__ == '__main__':
    a = ['bias']
    b = 's'
    print(b in a[0])