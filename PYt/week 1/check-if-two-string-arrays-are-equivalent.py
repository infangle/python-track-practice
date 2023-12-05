class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''.join(word1)
        w2 = ''.join(word2)
        if len(w1) != len(w2):
            return False
        else:
            for c in range(len(w1)):
                if w1[c] != w2[c]:
                    return False
                    break
            return True
        