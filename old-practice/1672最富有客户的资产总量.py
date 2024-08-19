'''
https://leetcode-cn.com/problems/richest-customer-wealth/
'''
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''
        l=[]
        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        return max(l)
        '''

        l=[]
        x=0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                x=x+accounts[i][j]
            l.append(x)
            x=0
        return max(l)
