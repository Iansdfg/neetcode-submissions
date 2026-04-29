MAP = {
    '2':["A", "B", "C"],
    '3':["D", "E", "F"],
    '4':["G", "H", "I"],
    '5':["J", "K", "L"],
    '6':["M", "N", "O"],
    '7':["P", "Q", "R", "S"],
    '8':["T", "U", "V"],
    '9':["W", "X", "Y", "Z"],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterCombinations = []
        if not digits:
            return letterCombinations
        self.dfs(digits, 0, [], letterCombinations)
        return letterCombinations

    def dfs(self, digits, index, path, letterCombinations):
        if len(path) == len(digits):
            print(path)
            letterCombinations.append(''.join(path))
            return 
        for i in range(index, len(digits)):
            # print(digits[i], MAP[digits[i]])
            for letter in MAP[digits[i]]:
                path.append(letter.lower())
                self.dfs(digits, i+1, path, letterCombinations)
                path.pop()

        