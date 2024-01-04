class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        op = 0

        while l < r:
            print(l, r)
            if sorted_nums[l] + sorted_nums[r] == k:
                l += 1
                r -= 1
                op += 1
            elif sorted_nums[l] + sorted_nums[r] < k:
                l += 1
            elif sorted_nums[l] + sorted_nums[r] > k:
                r -= 1
           

        return op