class Solution:
    def largestOddNumber(self, num: str) -> str:
        beg = 0
        end = len(num) - 1
        while end >= beg:
            if int(num[end]) % 2 != 0:
                return num[beg:end+1]
            else:
                end -= 1
        return ""

        