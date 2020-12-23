# author : 'wangzhong';
# date: 26/11/2020 00:21

"""
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
输出："a a a a a a a a bbb baba a"

"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        temp = sentence.split(" ")
        for i in range(len(temp)):
            replace = ""
            for j in range(len(dictionary)):
                if temp[i].startswith(dictionary[j]) and (len(dictionary[j]) < len(replace) or len(replace) < 1):
                    replace = dictionary[j]
            if len(replace) > 0:
                temp[i] = replace
        return " ".join(temp)

    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        rootSet = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootSet:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))


if __name__ == '__main__':
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    solution = Solution()
    new = solution.replaceWords2(dictionary, sentence)
    print(new)
