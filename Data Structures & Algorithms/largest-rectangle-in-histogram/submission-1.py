class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]

        index_stack = []
        max_a = 0
        curr_h = 1
        for i, h in enumerate(heights):
            if not index_stack:
                index_stack.append(i)
            else:
                while h < heights[index_stack[-1]]:
                    curr_h_i = index_stack.pop()
                    curr_h = heights[curr_h_i] 
                    w = i - index_stack[-1] - 1 
                    area = w * curr_h
                    max_a = max(max_a, area)

                index_stack.append(i)

        return max_a
