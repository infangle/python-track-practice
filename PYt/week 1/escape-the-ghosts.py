class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghostD = []
        myD = abs(target[0] - 0) + abs(target[1] - 0)
        for g in ghosts:
            ghostD.append(abs(target[0] - g[0]) + abs(target[1] - g[1]))

        for d  in ghostD:
            if myD >= d:
                return False
        return True
        