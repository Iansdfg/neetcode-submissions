class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        max_area = self.getArea(start, end, heights)
        while start < end:
            if heights[start] <= heights[end]:
                start += 1 
            elif heights[start] > heights[end]:
                end -= 1
            area = self.getArea(start, end, heights)
            max_area = max(max_area, area)
            print(start, end, max_area)
        return max_area
            
    def getArea(self, left, right, heights) -> int:
        area = (right - left) * min(heights[left], heights[right])
        return area
        