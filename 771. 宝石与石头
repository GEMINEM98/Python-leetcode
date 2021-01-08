
# https://leetcode-cn.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        # 先把石头数量用字典存起来，然后计算出数量，遍历字典，求出和：
        d={} # 定义一个空字典
        count=0 # 计数
        for i in range(len(stones)):
            d[stones[i]]=d.get(stones[i],0)+1  
            # 字典的dict.get(key,default=None)函数，
            # 返回指定键key的值，如果值不存在，那么返回default的默认值None.
        for j in range(len(jewels)):
            if jewels[j] in d.keys():
                count+=d[jewels[j]]
        return count
        '''

        return sum(stones.count(i) for i in jewels)


