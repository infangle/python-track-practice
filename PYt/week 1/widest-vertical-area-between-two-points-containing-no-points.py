class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda a: a[0])

        res = 0

        for i in range(1, len(points)):
            res = max(res, abs(points[i][0] - points[i-1][0]))

        return res
