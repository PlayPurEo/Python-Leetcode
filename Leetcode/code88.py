# author : 'wangzhong';
# date: 25/11/2020 22:33

"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
不可以返回一个新的数组，内存地址必须相同
"""

import random
from typing import List


def mergeArray(a: List, m: int, b: List, n: int) -> None:
    acopy = a[:m]
    a[:] = []
    start1 = 0
    start2 = 0
    while start1 < m and start2 < n:
        if acopy[start1] < b[start2]:
            a.append(acopy[start1])
            start1 += 1
        else:
            a.append(b[start2])
            start2 += 1
    if start1 < m:
        a[start1 + start2:] = acopy[start1:]
    else:
        a[start1 + start2:] = b[start2:]


if __name__ == '__main__':
    a = random.sample(range(0, 100), 15)
    b = random.sample(range(0, 100), 10)
    a.sort()
    b.sort()
    print(a)
    print(b)
    m = 5
    n = len(b)
    mergeArray(a, m, b, n)
    print(a)
