class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = 0
        s = 0
        inter = []
        while f < len(firstList) and s < len(secondList):
    
            if secondList[s][0] <= firstList[f][1] and firstList[f][0] <= secondList[s][1]:
                inter.append([max(firstList[f][0],secondList[s][0]), min(firstList[f][1],secondList[s][1])])

            if secondList[s][1] > firstList[f][1]:
                f += 1
            else:
                s += 1

        return inter
