class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        row_num = {}
        ans = []
        for word in words:
            w = set(word.lower())
            if w <= first_row or w <= second_row or w <= third_row :
                ans.append(word)

        return ans
