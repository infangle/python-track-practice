class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        input - string
        output - length of substring - (longest substring without repeating characters)
        ds - sliding window with dynamic size(longest)
        set - avoid duplcates
        tc = O(n)
        sc = O(n)
        """
        chars = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
            chars[s[r]] = r
            res = max(res, r - l + 1)
        return res

        