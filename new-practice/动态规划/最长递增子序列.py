
'''
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        maxNum = 1
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[j] < nums[i]:
                    dp[i] =max(dp[i], dp[j]+1)
                maxNum = max(maxNum, dp[i])
                j -= 1
        return maxNum

if __name__ == '__main__':
    print(Solution().lengthOfLIS([0]))









