DIRCTION = [(0,1),(1,0),(0,-1),(-1,0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    visited[row][column] = 1
                    if self.dfs(board, word, visited, 0, row, column):
                        return True
                    visited[row][column] = 0
        return False

    def dfs(self, board, word, visited, index, row, column):
        if board[row][column] != word[index]:
            return False 
        if index >= len(word):
            return False
        if index == len(word) - 1:
            return True

        for x, y in DIRCTION:
            if not self.is_valid(board, visited, row + x, column + y):
                continue 
            visited[row + x][column + y] = 1 
            if self.dfs(board, word, visited, index+1, row + x, column + y):
                return True 
            visited[row + x][column + y] = 0
        return False

        
    def is_valid(self, board, visited, x, y):
        if x < 0 or x >= len(board):
            return False 
        if y <0 or y>= len(board[0]):
            return False 
        if visited[x][y]:
            return False 
        return True 
        