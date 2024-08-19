
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

class Solution:
    def addDigits(self, num: int) -> int:
        if num % 10 == num:
            return num

        res = 0
        str_num = str(num)
        for i in str_num:
            res += int(i)
        return self.addDigits(int(res))



if __name__ == '__main__':
    print(Solution().addDigits(242542))