class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans = set()
        for ch in s:
            ans.add(ch)

        return len(ans)

