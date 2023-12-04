class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            ans = ans + word1[i]
            ans = ans + word2[j]
            i+=1
            j+=1
        ans = ans + word1[i:]
        ans = ans + word2[j:]
        return ans

        