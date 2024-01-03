class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if sorted_nums[i] + sorted_nums[j] < target:
                    count += 1
        return count
                

