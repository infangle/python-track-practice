class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        for c in costs:
            if c > coins:
                break
            else:
                coins -= c
                bars += 1
        return bars
                
