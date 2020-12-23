# author : 'wangzhong';
# date: 05/12/2020 21:36

"""
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

假设其中出现次数最多的种类的次数为maxExec
次数最多的种类的数量为maxCount
执行时间最短，就是将次数最多的依次排开，把中间的冷却时间n排满，不管是排其他任务还是待命
这样算出来的情况可能会小于数组长度，所以两个中间取最大值
"""
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxExec = max(count.values())
        # maxCount = 0
        # for i in count:
        #     if count[i] == maxExec:
        #         maxCount += 1
        maxCount = sum(1 for i in count if count[i] == maxExec)
        shortestTime = (maxExec - 1) * (n + 1) + maxCount
        return max(shortestTime, len(tasks))


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    print(Solution().leastInterval(tasks, 2))
