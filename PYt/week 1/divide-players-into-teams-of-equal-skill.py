class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skills = sorted(skill)

        l = 0
        r = len(skills) - 1

        chemistry = 0

        while l < r:
            print(l, r)
            if skills[l] + skills[r] == skills[l+1] + skills[r-1]:
                chemistry += skills[l] * skills[r]
                l += 1
                r -= 1
            else:
                return -1
        return chemistry
        