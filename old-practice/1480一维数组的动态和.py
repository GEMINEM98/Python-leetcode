'''
https://leetcode-cn.com/problems/running-sum-of-1d-array/
'''
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i];
        return nums
        '''
        
        x=0
        l=[]
        for i in range(len(nums)):
            x=x+nums[i]
            l.append(x)
        return l

        
