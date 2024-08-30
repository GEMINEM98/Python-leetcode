'''
26. 删除有序数组中的重复项

给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1

        left = 0
        right = 1

        while right < len(nums):
            if nums[right] != nums[left]:
                nums[left] = nums[right]
                left += 1
                
            right += 1

        return left + 1


def main():
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    solution = Solution()
    length = solution.removeDuplicates(nums)
    print(f"Length of array after removing duplicates: {length}")
    print(f"Array after removing duplicates: {nums[:length]}")

if __name__ == "__main__":
    main()



