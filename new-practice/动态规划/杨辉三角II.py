'''
119. 杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        matrix = list()
        for i in range(rowIndex+1):
            row = list()
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(matrix[i-1][j-1]+matrix[i-1][j])
            matrix.append(row)
        return matrix[rowIndex]

if __name__ == '__main__':
    print(Solution().getRow(3))




