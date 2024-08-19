'''
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
'''
from typing import List

'''
1、创建一个dp数组，dp数组最大下标等于总金额的大小
2、遍历dp数组，遍历coins数组
3、如果dp数组的当前金额(下标)>=coin，dp[i] = min(dp[i-coin] + 1, dp[i])，注意，如果当前金额减去coin后的金额的硬币数是-1，那么当前coin也是-1，直接继续遍历下一个coin
4、遍历完coins后，如果dp[i]没有被覆盖，说明不能完全兑换成硬币，直接给-1
5、输出dp数组最后一个数的大小，就是总金额的硬币数
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    if dp[i-coin] == -1:
                        continue
                    else:
                        dp[i] = min(dp[i-coin] + 1, dp[i])
            if dp[i] == float('inf'):
                dp[i] = -1
        print(dp)
        return dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([2], 3))


