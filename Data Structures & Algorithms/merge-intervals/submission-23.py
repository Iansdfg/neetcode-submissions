class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, interval in enumerate(intervals):
            if i == 0:
                temp = interval
            else:
                if self.is_overlap(temp, interval):
                    temp = self.merge_two(temp, interval)
                else:
                    res.append(temp)
                    temp = interval
        res.append(temp)
        return res 
    
    def is_overlap(self, temp, interval):
        return temp[1] >= interval[0]

    def merge_two(self, temp, interval):
        temp[1] = max(temp[1], interval[1])
        return temp

