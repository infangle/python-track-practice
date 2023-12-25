class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = 0
        primaryd = 0
        while i < len(mat) and j < len(mat[0]):
            primaryd += mat[i][j]
            i += 1
            j += 1

        i = 0
        j = len(mat[0]) - 1
        secondaryd = 0
        while i < len(mat) and j >= 0:
            secondaryd += mat[i][j]
            i += 1
            j -=1
        if len(mat) % 2 == 0:
            return primaryd + secondaryd
        else:
            mid = (len(mat) - 1) // 2
            return primaryd + secondaryd - mat[mid][mid]

        
        