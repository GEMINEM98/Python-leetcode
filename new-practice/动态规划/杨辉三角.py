

'''
118. 杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = list()
        for i in range(numRows):
            row = list()
            for j in range(i+1):
                if j == 0 or i == j:
                    row.append(1)
                else:
                    row.append(matrix[i-1][j-1]+matrix[i-1][j])
            matrix.append(row)
        return matrix

if __name__ == '__main__':
    print(Solution().generate(4))






