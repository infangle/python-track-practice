class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        l = 0
        r = len(p) -1

        boats = 0
        while l < r:
            if p[l] + p[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else: 
                boats += 1
                r -= 1
        if l == r:
            boats += 1
                    
        return boats