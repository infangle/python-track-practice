class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = list(s)
        for i, c in enumerate(result):
            if indices[i] == i:
                continue
            move, j = c, indices[i]
            while j != i:
                result[j], move = move, result[j]
                indices[j], j = j, indices[j]
            result[i] = move
        return "".join(result)