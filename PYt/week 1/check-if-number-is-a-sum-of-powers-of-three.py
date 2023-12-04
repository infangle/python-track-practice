class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(14, -1, -1):
            num = 3**i
            if n - num >=0:
                n -= num
            if n == 0:
                return True
        return False