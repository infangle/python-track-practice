class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        nonFlip = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                nonFlip.add(fronts[i])


        res = inf
        for card in fronts + backs:
            if card not in nonFlip:
                res = min(res, card)

        if res != inf:
            return res
        else:
            return 0