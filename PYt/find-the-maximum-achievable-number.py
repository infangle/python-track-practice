class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = num
        while t:
            num +=1
            x +=2
            t-=1 
        return x