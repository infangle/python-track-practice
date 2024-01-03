class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        greed = sorted(g)
        cookies = sorted(s)
        l = 0
        r = 0
        while l < len(g) and r < len(s):
            if greed[l] <= cookies[r]:
                content += 1
                l += 1
            r += 1

        return content