class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums.copy()
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans