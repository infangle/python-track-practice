class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        even = True
        Dtrav = []
        c = 0
        r = 0
        for _ in range(len(mat) * len(mat[0])):
            if even:
                Dtrav.append(mat[r][c])
                if r-1 < len(mat) and r-1 >= 0:
                    if c + 1 < len(mat[0]):
                        c += 1
                        r -= 1
                    else:
                        r += 1
                        even = False
                else:
                    if c+1 < len(mat[0]) and c+1 >= 0:
                        c += 1
                    else:
                        r += 1
                    even = False
            else:
                Dtrav.append(mat[r][c])
                if c - 1 < len(mat[0]) and c-1 >=0:
                    if r + 1 < len(mat):
                        c -= 1
                        r += 1
                    else:
                        c += 1
                        even =True
                else:
                    if r + 1 < len(mat) and r+1 >=0:
                        r += 1
                    else:
                        c += 1
                    even = True

        return Dtrav
        
        