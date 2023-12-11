class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = {}
        l = len(arr)
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        for k, v in counts.items():
            if v >  l*0.25 :
                return k      