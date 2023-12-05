class Solution:
    def freqAlphabets(self, s: str) -> str:
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = len(s)-1
        result = []
        while i >= 0:
            if s[i] == '#':
                result.append(alpha(s[i-2:i]))
                i -= 3
            else:
                result.append(alpha(s[i]))
                i -= 1
        return "".join(reversed(result))