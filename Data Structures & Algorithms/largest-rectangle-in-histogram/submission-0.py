class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                indx, height = stack.pop()
                maxArea = max(maxArea, height * (idx-indx))
                start = indx
            stack.append((start, h))
        
        for idx, h in stack:
            maxArea = max(maxArea, h * (len(heights) - idx))
        return maxArea