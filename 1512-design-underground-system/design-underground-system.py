from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.passengers = defaultdict(lambda : ("", 0))
        self.calculations = defaultdict(lambda: [0, 0.0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st_loc, st_t = self.passengers[id]
        if (st_loc, stationName) in self.calculations:
            count, avg = self.calculations[(st_loc, stationName)]
            final_avg = ((count * avg) + (t - st_t)) / (count + 1)
            self.calculations[(st_loc, stationName)] = (count + 1, final_avg)
        else:
            self.calculations[(st_loc, stationName)] = (1, t - st_t)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.calculations[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)