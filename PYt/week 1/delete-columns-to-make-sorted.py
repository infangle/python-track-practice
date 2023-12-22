class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        transpose = []
        for col in range(len(strs[0])):
            t_row = []
            for row in range(len(strs)):
                t_row.append(strs[row][col])
            transpose.append(t_row)
        count = 0
        for c in transpose:
            if (sorted(c) != c):
                count += 1

        return count
        