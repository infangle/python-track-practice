class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ans = []
        for i in range(len(digits)):
            num *= 10
            num += digits[i]

        num += 1
        number = str(num)
        for d in number:
            ans.append(int(d))
        return ans