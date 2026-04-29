from collections import deque,defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_indgree = {i:0 for i in range(numCourses)}
        start_end = defaultdict(list)
        for start,end in prerequisites:
            start_end[start].append(end)
            node_indgree[end] = node_indgree.get(end, 0) + 1

        start = [node for node in node_indgree if node_indgree[node]==0]
        queue = deque(start)


        order = []
        while queue:
            curr_couse = queue.popleft()
            order.append(curr_couse)
            for next_couse in start_end[curr_couse]:
                node_indgree[next_couse] -= 1
                if node_indgree[next_couse] == 0:
                    queue.append(next_couse)

        return len(order) == numCourses
