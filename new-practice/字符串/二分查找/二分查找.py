'''
704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right =len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1


def main():
    # 测试用例
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    # 创建Solution实例
    solution = Solution()

    # 调用search方法并输出结果
    result = solution.search(nums, target)

    print(f"在数组 {nums} 中查找数字 {target} 的结果索引是: {result}")


if __name__ == "__main__":
    main()

