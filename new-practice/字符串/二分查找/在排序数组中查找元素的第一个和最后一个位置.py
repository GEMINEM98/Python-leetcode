
'''
34. 在排序数组中查找元素的第一个和最后一个位置

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left < 0 or left >= len(nums):
            return [l, r]
        if nums[left] == target:
            l = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or right >= len(nums):
            return [l, r]
        if nums[right] == target:
            r = right

        return [l, r]


def main():
    # 测试用例
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # 创建Solution实例
    solution = Solution()

    # 调用searchRange方法并输出结果
    result = solution.searchRange(nums, target)

    print(f"在数组 {nums} 中，目标值 {target} 的起始和结束位置是: {result}")


if __name__ == "__main__":
    main()


