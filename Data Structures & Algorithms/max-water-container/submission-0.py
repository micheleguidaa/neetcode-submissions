class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        current_area = 0
        max_area = current_area
        while left < right:
            lenght = (right - left)
            min_height = min(heights[left], heights[right])
            current_area = lenght * min_height
            if current_area > max_area:
                max_area = current_area
            if min_height == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
        