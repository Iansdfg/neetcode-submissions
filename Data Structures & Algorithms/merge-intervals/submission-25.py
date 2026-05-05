class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        slow = 0
        for i, interval in enumerate(intervals):
            if i == 0:
                temp = interval
            else:
                if self.is_overlap(temp, interval):
                    temp = self.merge_two(temp, interval)
                else:
                    intervals[slow] =  temp
                    slow += 1 
                    temp = interval
        intervals[slow] =  temp
        return intervals[:slow+1] 
    
    def is_overlap(self, temp, interval):
        return temp[1] >= interval[0]

    def merge_two(self, temp, interval):
        temp[1] = max(temp[1], interval[1])
        return temp

