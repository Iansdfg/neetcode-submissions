class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = (right - left)*min(heights[left],heights[right])
        while left < right:
            if heights[left] <= heights[right]:
                left += 1 
            elif heights[left] > heights[right]:
                right -= 1 
            max_area = max(max_area, (right - left)*min(heights[left],heights[right]))
        return max_area

        