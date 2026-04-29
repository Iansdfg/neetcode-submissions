import heapq 
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted( (value, index) for index, value in enumerate(queries))
        res = [-1 for i in range(len(queries))]
        print(sorted_queries)
        print(intervals)
        mini_queue = []
        interval_index = 0

        for query, query_index in sorted_queries:
            print(query, query_index)
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                left, right = intervals[interval_index]
                heapq.heappush(mini_queue, (right - left + 1, right))
                interval_index += 1 

            while mini_queue and mini_queue[0][1] < query:
                heapq.heappop(mini_queue)
            
            if mini_queue:
                res[query_index] = mini_queue[0][0]

        return res

