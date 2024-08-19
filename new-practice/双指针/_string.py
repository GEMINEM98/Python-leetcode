'''

字符串的使用

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成


'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: 定义需要维护的变量, 本题求最大长度，所以需要定义max_len, 该题又涉及去重，因此还需要一个哈希表
        max_len, hashmap = 0, {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3
            # 更新需要维护的变量 (max_len, hashmap)
            # i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end - start + 1)

            # Step 4:
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        # Step 5: 返回答案 (最大长度)
        return max_len



if __name__ == '__main__':
    s = "fsdfsuohfavf"
    print(Solution().lengthOfLongestSubstring(s))






