class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        zeros = 0
        sub = 0
        if nums[l] == 0:
            zeros += 1
        while l < r and r < len(nums):
            if nums[r] == 0:
                zeros += 1
                   
            if zeros > 1:
                # sub = max(sub, r - l-1)
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            r += 1
            sub = max(sub, r - l-1)
        return sub
            
             

        