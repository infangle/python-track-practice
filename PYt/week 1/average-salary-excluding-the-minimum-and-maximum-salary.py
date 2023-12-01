class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = 0
        d = 0.00000
        for s in range(1, len(salary)-1):
            total += salary[s]
            d+=1
        return(total/d)
        