class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for element in nums:
            result += [subset + [element] for subset in result]
        return result
        
