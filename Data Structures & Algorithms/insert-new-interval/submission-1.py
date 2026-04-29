class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False 
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)

            elif newInterval[1] < interval[0]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True 
                res.append(interval)

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            print(res, newInterval)

        if not inserted:
            res.append(newInterval) 
        return res