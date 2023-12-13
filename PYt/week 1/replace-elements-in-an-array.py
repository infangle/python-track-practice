class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # time complexity : O(n + m)
        #space complexity : O(n)
        numbers = {}
        for i, n in enumerate(nums):
            numbers[n] = i

        for prev, new in operations:
            index = numbers[prev]
            nums[index] = new
            numbers[new] = index
            del numbers[prev]

        return nums