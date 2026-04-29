"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for intervals in intervals:
            events.append((intervals.start, 1))
            events.append((intervals.end, -1))

        events.sort()
        action = 0
        res = 0 
        for time, delta in events:
            action += delta
            res = max(res, action)
        return res

        