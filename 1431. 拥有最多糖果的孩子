
# https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        maxnum=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<maxnum:
                l.append(bool(False))
            else:
                l.append(bool(True))
        return l

