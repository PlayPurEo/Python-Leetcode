# author : 'wangzhong';
# date: 22/12/2020 15:49

"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ["1"]
        if n == 1:
            return ans[0]
        for i in range(1, n):
            s = ""
            num = ans[i - 1][0]
            times = 1
            for j in range(1, len(ans[i - 1])):
                if ans[i - 1][j] == ans[i - 1][j - 1]:
                    times += 1
                else:
                    s += str(times) + str(num)
                    num = ans[i - 1][j]
                    times = 1
            s = s + str(times) + str(num)
            ans.append(s)
        return ans[-1]