from typing import List


# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 从后往前确定的比较快


        cur1 = m - 1
        cur2 = n - 1
        end = len(nums1) - 1
        while cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] > nums2[cur2]:
                nums1[end] = nums1[cur1]
                cur1 -= 1
            else:
                nums1[end] = nums2[cur2]
                cur2 -= 1
            end -= 1
        if cur1 == -1:
            nums1[0:end+1] = nums2[0:cur2+1]
        print(nums1)

if __name__ == '__main__':
    Solution().merge([4,5,6,0,0,0],3,[1,2,3],3)