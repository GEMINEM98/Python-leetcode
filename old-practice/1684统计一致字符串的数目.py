from typing import List


# https://leetcode-cn.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # 用集合进行去重
        st=set(allowed)
        count=0
        for i in range(len(words)):
            tmp=set(words[i])
            if st>=tmp:
                count+=1
        return count


