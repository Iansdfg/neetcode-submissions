DIRCTION = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [0 for i in range(n)]
        permutations = []
        self.dfs(n, visited, [], permutations)
        return permutations
    

    def dfs(self, n, visited, path, permutations):
        if len(path) > n:
            return 
        if len(path) == n:
            board = self.draw(path)
            permutations.append(board)
            return  
        for i in range(n):
            if visited[i]:
                continue
            if not self.is_valid(path, i):
                continue
            path.append(i)
            visited[i] = 1 
            self.dfs(n, visited, path, permutations)
            visited[i] = 0
            path.pop()

    def is_valid(self, path, i):
        row, col = len(path), i
        for prev_row, prev_col in enumerate(path):
            if abs(prev_row - row) == abs(prev_col - col):
                return False 
        return True 
    
    def draw(self, path):
        board = [['.' for _ in range(len(path))] for _ in range(len(path))]
        res = []
        for row, col in enumerate(path):
            board[row][col] = 'Q'
        for row in board:
            res.append(''.join(row))
        print(res)
        return res


    

        

        