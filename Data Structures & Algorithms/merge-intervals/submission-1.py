class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1][1] >= interval[0]:
                    res[-1][0] = min(res[-1][0], interval[0])
                    res[-1][1] = max(res[-1][1], interval[1])
                else:
                    res.append(interval)
            print(res)
        return res 

    def is_overlap(self, interval1, interval2):
        if interval1[1] <= interval2[0]:
            return True 
        else:
            return False 

        