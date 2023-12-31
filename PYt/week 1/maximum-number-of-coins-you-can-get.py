class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        res = 0

        b,a = 0, len(piles)-1
        while b < a:
            a -=1
            res += piles[a]
            a -= 1
            b += 1

        return res
            
        