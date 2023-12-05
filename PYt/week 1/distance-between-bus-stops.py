class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = min(start, destination)
        m = max(start, destination)

        return min(sum(distance[n:m]), sum(distance[m:] + distance[:n]))
        