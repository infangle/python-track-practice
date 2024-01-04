class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = {}
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l < r:
                tsum = a + nums[l] + nums[r]
                if tsum > target:
                    r-=1
                elif tsum < target:
                    l+=1
                else:
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                dif = abs(target - tsum )
                res[dif] = tsum
        
        diff = inf
        for d in res:
            if d < diff:
                diff = d
                ans = res[d]
        return ans