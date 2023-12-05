class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split()
        longest = max(words, key=len)
        ans = [[] for _ in range(len(longest))]
        for w in words:
            for i in range(len(longest)):
                ans[i].append(w[i] if i < len(w) else ' ')
        return [''.join(x).rstrip() for x in ans]

