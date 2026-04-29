class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root_of_i = [i for i in range(n)]

        for edge in edges:
            sm_node = min(edge)
            lg_node = max(edge)
            
            root_sm_node = root_of_i[sm_node]
            if root_of_i[lg_node] == root_sm_node:
                continue
            root_of_i[lg_node] = root_sm_node
            n -= 1
        return n





        