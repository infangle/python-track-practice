class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq =  Counter(nums)
        for f in freq.values():
            if f >= 2:
                return True
        return False
        