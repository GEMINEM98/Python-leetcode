'''
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(1, len(s) + 1):
            for i in range(j - 1, -1, -1):
                if s[i:j] in wordDict and dp[i] == True:
                    dp[j] = True
                    break
        return dp[-1]


if __name__ == '__main__':

    print(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]))




