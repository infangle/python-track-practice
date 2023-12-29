class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return "0"

        nums = list(map(str, nums))
        if len(nums) < 2:
            return ''.join(nums)
        for i in range(len(nums) - 1):
            j = i + 1
            while i < len(nums) and j < len(nums):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return "".join(nums)
            
             
