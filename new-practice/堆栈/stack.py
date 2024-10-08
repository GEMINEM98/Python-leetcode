
'''
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pipei = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in pipei:
                if stack and stack[-1] == pipei[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == '__main__':
    print(Solution().isValid("{[(){[()]}]}"))