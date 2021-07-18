
"""
Beats 22% in terms of runtime
Beats 75% in terms of memory
First time submission succesful.
Came up with a solution in 10 minutes and 27 seconds.
"""


class UndergroundSystem:

    def __init__(self):
        self.times_dict: Dict[Tuple[str, str], List[int]] = dict()
        self.check_ins: Dict[int, Tuple[str, int]] = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        self.times_dict.setdefault(
            (start_station, stationName), []).append(t-start_time)
        self.check_ins.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times_list = self.times_dict[(startStation, endStation)]
        return sum(times_list)/len(times_list)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
