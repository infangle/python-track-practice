class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s) - 1
        while beg < end:
            temp = s[beg]
            s[beg] = s[end]
            s[end] = temp
            beg += 1
            end -= 1

        