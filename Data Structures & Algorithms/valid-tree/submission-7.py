class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return len(edges) == 0

        if len(edges) == 0 or n == 0 or len(edges) < n-1:
            return False

        head_tail = dict()
        for head, tail in edges:
            if head in head_tail:
                head_tail[head].append(tail)
            else:
                head_tail[head] = [tail]
            if tail in head_tail:
                head_tail[tail].append(head)
            else:
                head_tail[tail] = [head]

        for i in range(n):
            no_cyc = self.dfs(None, i, head_tail, set())
            if no_cyc == False:
                return False 

        return True 


    def dfs(self, prev, node, node_nighbor, visited):
        if node in visited:
            return False 

        for next_node in node_nighbor[node]:
            if next_node == prev:
                continue
            visited.add(node)
            no_cyc = self.dfs(node, next_node, node_nighbor, visited)
            if no_cyc == False:
                return False
            visited.remove(node)


        