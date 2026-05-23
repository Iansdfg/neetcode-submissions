from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_indegree = {i:0 for i in range(numCourses)}
        start_end = defaultdict(list)
        for after, before in prerequisites:
            start_end[after].append(before)
            node_indegree[before] = node_indegree.get(before,0)+1 

        queue = deque([])
        for node in node_indegree:
            if node_indegree[node] == 0:
                queue.append(node)


        top_order = []
        while queue:
            curr = queue.popleft()
            top_order.append(curr)
            for next_node in start_end[curr]:
                node_indegree[next_node] -= 1
                if node_indegree[next_node] == 0:
                    queue.append(next_node)
        
        return len(top_order) == numCourses
        