class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        
        n = len(nums)
        for i in range(n):
            if i not in visited:
                # running for only non visited nodes 
                local = set()
                while True:
                    if i in local:
                        return True
                    # if i already present in local 
                    visited.add(i)
                    local.add(i)
                    # handle the self case
                    # dont add the self nodes 
                    prev,i = i , (i+nums[i])%n
                    if prev == i:
                        break
                    # if prev and curr node has different sign , dont append it 
                    if (nums[i]>0)!=(nums[prev]>0):
                        break
        return False
                        