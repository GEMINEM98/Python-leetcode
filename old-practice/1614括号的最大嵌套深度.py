
# https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        left=0
        if s=="":
            return 0
        elif len(s)==1 and s[0]!='(' and s[0]!=')':
            return 0
        else:
            for i in range(len(s)):
                if s[i]=='(':
                    left+=1
                    if left>depth:
                        depth=left
                if s[i]==')':
                    left-=1
            return depth

        
