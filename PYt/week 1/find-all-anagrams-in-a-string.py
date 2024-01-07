class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l = 0
        k = len(p)
        p_sorted = ''.join(sorted(p))

        for r in range(k - 1, len(s)):
            window = s[l:r + 1]
            window_sorted = ''.join(sorted(window))

            if window_sorted == p_sorted:
                ans.append(l)

            l += 1

        return ans