from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_indgree = {i:0 for i in range(numCourses)}
        start_end = defaultdict(list)

        for start, end in prerequisites:
            course_indgree[start] += 1 
            start_end[end].append(start)
        print(course_indgree, start_end)

        start = []
        for key in course_indgree:
            if course_indgree[key] == 0:
                start.append(key)
        queue = deque(start)


        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next_course in start_end[curr]:
                course_indgree[next_course] -= 1 
                if course_indgree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []


        