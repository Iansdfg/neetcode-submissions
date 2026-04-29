class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []
        self.dfs(s, 0, [], substrings)
        return substrings


    def dfs(self, s, index, path, substrings):
        if index > len(s):
            return 

        if index == len(s):
            substrings.append(path[:])

        for i in range(index+1, len(s)+1):
            if s[index:i] != s[index:i][::-1]:
                continue 
            path.append(s[index:i])
            self.dfs(s, i, path, substrings)
            path.pop()
        