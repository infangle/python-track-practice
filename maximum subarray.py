class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarr = nums[0]
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum+=n
            subarr = max(subarr, sum)
        return subarr       
