class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = False
        y = str(x)
        x = y[::-1]
        for i in range(len(y)):
            if y[i] == x[i]:
                ans = True
            else:
                ans = False
                break
        return ans