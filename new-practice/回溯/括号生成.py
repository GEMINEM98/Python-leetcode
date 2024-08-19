'''

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

一般回溯的问题有三种：

Find a path to success 有没有解
Find all paths to success 求所有解
求所有解的个数
求所有解的具体信息
Find the best path to success 求最优解

'''
import string
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        self.dfs(res, n, n, path)
        return res

    def dfs(self, res: list, left: int, right: int, path: string) -> None:
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + "(")
        if left < right:
            self.dfs(res, left, right - 1, path + ")")


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
