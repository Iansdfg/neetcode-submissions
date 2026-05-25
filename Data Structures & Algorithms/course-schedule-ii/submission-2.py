from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_course = defaultdict(list)
        course_indegree = {i:0 for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_course[pre].append(course)
            course_indegree[course] = course_indegree.get(course, 0) + 1 

        queue = deque([])
        for course,indegree in course_indegree.items():
            if indegree == 0:
                queue.append(course)

        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next_course in pre_course[curr]:
                course_indegree[next_course] -= 1 
                if course_indegree[next_course] == 0:
                    queue.append(next_course)
        return order if len(order) == numCourses else []

        