# author : 'wangzhong';
# date: 10/12/2020 13:43


"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        n = len(bills)
        for i in range(n):
            if bills[i] == 5:
                five += 1
                continue
            if bills[i] == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
                continue
            if bills[i] == 20:
                if ten > 0 and five > 0:
                    five = five - 1
                    ten = ten - 1
                elif five > 2:
                    five = five - 3
                else:
                    return False
        return True