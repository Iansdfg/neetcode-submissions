"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        active = 0
        queue = []
        res = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            queue.append((start, 1))
            queue.append((end, -1))

        queue.sort()
        for time, action in queue:
            active += action
            res = max(res, active)
        return res



        