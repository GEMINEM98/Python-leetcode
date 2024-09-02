from typing import List
from builtins import str


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        strs.sort(reverse=True)
        s1 = strs[0]
        s2 = strs[len(strs) - 1]
        i = 0
        j = 0
        res = ""
        while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
            res += s1[i]
            i += 1
            j += 1

        return res


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort(key=lambda x: len(x))
#         n = len(strs[0])
#         l = 0
#
#         for i in range(n):
#             t = strs[0][i]
#
#             same = True
#             for s in strs:
#                 if t != s[i]:
#                     same = False
#                     break
#             if same:
#                 l += 1
#             else:
#                 break
#
#         return strs[0][:l]


if __name__ == '__main__':
    # str = ["flower", "flow", "flight"]
    str = ["cir", "car"]
    print(Solution().longestCommonPrefix(str))
