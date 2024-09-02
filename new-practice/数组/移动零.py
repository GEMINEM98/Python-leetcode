'''
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
        return


def main():
    nums = [0, 1, 0, 3, 12]
    print(f"Original array: {nums}")

    solution = Solution()
    solution.moveZeroes(nums)

    print(f"Array after moving zeroes: {nums}")


if __name__ == "__main__":
    main()

