from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        new_nums = permutations(nums)
        return new_nums
    
        
