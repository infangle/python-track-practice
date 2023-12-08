class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = []
        for n in nums:
            if n < 0 :
                negative.append(n)
            else:
                positive.append(n)
        for i in range(len(negative)):
            res.append(positive[i])
            res.append(negative[i])
        return res

