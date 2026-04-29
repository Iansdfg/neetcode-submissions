class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        left, right = 1, max(piles)

        while left + 1 < right:
            mid = (left + right)//2
            if self.can_finish(piles, mid, h):
                right = mid
            else:
                left = mid 
        if self.can_finish(piles, left, h):
            return left
        else:
            return right



    def can_finish(self, piles, k, h):
        time = 0
        for pile in piles:
            if pile < k:
                time += 1 
            else:
                if pile%k == 0:
                    time += pile//k
                else:
                    time += pile//k + 1 
        return time <= h

