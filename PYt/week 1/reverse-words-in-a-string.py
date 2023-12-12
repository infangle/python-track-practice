class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = list(s.split())
        rev_string_list = string_list[::-1]
        rev_s = " ".join(rev_string_list)
        return rev_s 
        