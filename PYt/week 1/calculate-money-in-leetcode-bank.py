class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7 #1
        n = n % 7 #3
        day = 1
        depo = 0
        for _ in range(weeks): #1
            depo += 7*(day + day+6) //2 #
            day += 1
        for i in range(n):
            depo += day
            day +=1


        return depo


        