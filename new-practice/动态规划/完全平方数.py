
'''
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''


class Solution:
    def numSquares(self, n: int) -> int:
        l = [float('inf')]*(n+1)
        l[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                l[i] = min(l[i-j*j]+1, l[i])
                j += 1
        # print(l)
        return l[n]

if __name__ == '__main__':
    print(Solution().numSquares(12))


