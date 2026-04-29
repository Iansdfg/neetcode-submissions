class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) -1 
        max_area = 0
        while start <= end:
            height = min(heights[start], heights[end])
            width = end - start
            area = height * width
            max_area = max(max_area, area)
            
            if heights[start] < heights[end]:
                start += 1 
            elif heights[start] > heights[end]:
                end -= 1
            else:
                end -= 1 
        return max_area
        
        