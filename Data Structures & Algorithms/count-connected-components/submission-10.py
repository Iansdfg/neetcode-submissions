class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]


        for edge in edges:
            sm = min(edge)
            lg = max(edge)
            
            root_sm = parent[sm]
            if parent[lg] == root_sm:
                continue
            parent[lg] = root_sm
            n -= 1
        return n





        