class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter  = {}
        res = 0
        for i in nums:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        for x in counter.values():
            res += int((x*(x-1))/2)
        return res

         
