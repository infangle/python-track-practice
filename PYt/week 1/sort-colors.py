class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
        