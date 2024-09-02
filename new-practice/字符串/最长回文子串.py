'''
5. 最长回文子串

给你一个字符串 s，找到 s 中最长的 回文 子串。

'''

class Solution:
    def Palindrome(selfself, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # --------------------------------------- 回文字符串有两种情况，需要将两种情况都算下
            s1 = self.Palindrome(s, i, i)
            s2 = self.Palindrome(s, i, i+1)
            # ---------------------------------------

            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res


def main():
    s = "babad"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(f"The longest palindromic substring in '{s}' is: '{result}'")

if __name__ == "__main__":
    main()



