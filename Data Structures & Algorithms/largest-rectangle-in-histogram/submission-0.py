class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]

        index_stack = []
        max_a = 0
        for i, h in enumerate(heights):
            if not index_stack:
                index_stack.append(i)
            else:
                while h < heights[index_stack[-1]]:
                    curr_h_i = index_stack.pop()
                    w = i - index_stack[-1] - 1 
                    area = w *  heights[curr_h_i] 
                    max_a = max(max_a, area)

                index_stack.append(i)

        return max_a
