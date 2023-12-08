class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)//3
        ans = []
        for n in nums:
            if nums.count(n) > freq:
                ans.append(n)
        return set(ans)
        