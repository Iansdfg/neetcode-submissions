class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res = res + '+&' + string
        return res


    def decode(self, s: str) -> List[str]:
        return s.split('+&')[1:]
