class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sublist = []
        if len(nums) == 2:
            freq, val = nums[0], nums[1]
            for _ in range(freq):
                sublist.append(val)
            return sublist

        for i in range(len(nums)//2):#2
            freq, val = nums[2*i], nums[2*i+1]# 62,64 
            for _ in range(freq):#62*64
                sublist.append(val)
            
        return sublist
        