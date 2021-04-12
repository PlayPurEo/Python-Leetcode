# author : 'wangzhong';
# date: 23/02/2021 13:42

"""
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
"""
from typing import List
import pandas as pd
import numpy as np


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        maxIncrease = increase = sum(c * g for c, g in zip(customers[:X], grumpy[:X]))
        for i in range(X, n):
            increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            maxIncrease = max(maxIncrease, increase)
        return total + maxIncrease


if __name__ == '__main__':
    df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=list("abcd"))
    print(df)
    df[5] = df.iloc[:,:].mean(axis=1)
    print(df)