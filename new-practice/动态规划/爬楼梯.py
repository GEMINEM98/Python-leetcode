'''
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
from functools import cache

#------------------------------------------------ 装饰器实现
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


#------------------------------------------------ dict代替装饰器
class Solution1:

    d = {}
    def climbStairs(self, n: int) -> int:
        if n in self.d:
            return self.d[n]

        if n == 0 or n == 1:
            self.d[n] = 1
            return 1

        self.d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.d[n]



if __name__ == '__main__':
    print(Solution().climbStairs(44))

    print(Solution1().climbStairs(44))
    print(Solution1().d)
