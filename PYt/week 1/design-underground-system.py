class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.total = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.check_in[id]
        route = (start, stationName)

        if route not in self.total:
            self.total[route] = [0, 0]

        self.total[route][0] += t - time
        self.total[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.total[(startStation, endStation)]
        return total / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)