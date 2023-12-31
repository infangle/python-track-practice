class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cur = 0
        pre = 1
        res = 0
        for i in range(len(flips)):
            cur += flips[i]
            if cur == pre:
                res += 1
            pre += (i+2)

        return res
        
        