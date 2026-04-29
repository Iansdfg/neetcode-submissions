class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        temp = []
        res = []
        for index, interval in enumerate(intervals):
            if index == 0:
                temp = interval 
            else:
                if self.is_overlap(temp, interval):
                    temp = self.merge_two(temp, interval)
                
                elif not self.is_overlap(temp, interval):
                    res.append(temp)
                    temp = interval
            
        res.append(temp)
        return res 

    def is_overlap(self, temp, interval):
        return temp[1] >= interval[0]

    def merge_two(self, temp, interval):
        return [min(temp[0], interval[0]), max(temp[1], interval[1])]
                

        