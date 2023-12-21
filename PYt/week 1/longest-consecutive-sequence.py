class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        numbers = list(set(nums))
        numbers.sort()
        prev, output = 1 , 1
        for i in range(1, len(numbers)):
            if numbers[i-1] + 1 == numbers[i]:
                prev += 1
            else:
                prev = 1
            output = max(prev, output)

        return output