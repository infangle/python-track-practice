class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num = 0
        numset = set(nums)
        for num in range(n+1):
            if num not in numset:
                return num