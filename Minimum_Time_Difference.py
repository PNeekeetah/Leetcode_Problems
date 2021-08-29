"""
14:29 minutes
67% runtime
61% memory
First time submission succesful
"""


def convert_to_minutes(time: str):
    hours, minutes = time.split(":")
    return int(hours)*60 + int(minutes)


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        TOTAL_MINUTES_IN_A_DAY = 1440
        for i in range(len(timePoints)):
            timePoints[i] = convert_to_minutes(timePoints[i])
        timePoints.sort()
        aux = timePoints[0]

        for i in range(len(timePoints)):
            if i == len(timePoints) - 1:
                timePoints[i] = (aux - timePoints[i]) % TOTAL_MINUTES_IN_A_DAY
            else:
                timePoints[i] = (timePoints[i + 1] -
                                 timePoints[i]) % TOTAL_MINUTES_IN_A_DAY

        return min(timePoints)
