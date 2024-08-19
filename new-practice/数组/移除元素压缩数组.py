'''

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        num = 0

        while i < j:
            if nums[j] == val:
                j -= 1
                num += 1
                continue
            if nums[i] != val:
                i += 1
                continue

            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            num += 1
            i += 1
            j -= 1

        if i == j and nums[i] == val:
            num += 1

        if num != 0:
            nums = nums[:len(nums)-num]

        return len(nums)


if __name__ == '__main__':
    res = Solution().removeElement([3, 1, 3], 3)
    print(res)
