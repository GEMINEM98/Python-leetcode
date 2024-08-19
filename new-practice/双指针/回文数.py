class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)==str(x)[::-1]
        strx = str(x)
        lenx = len(strx)
        i, j = 0, lenx - 1
        res = True
        while i < j:
            if strx[i] == strx[j]:
                i += 1
                j -= 1
            else:
                return False
        return res

if __name__ == '__main__':
    x = 12165
    print(Solution().isPalindrome(x))
