class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]

            if h_left < h_right:
                current_water = h_left * (right - left)
                if current_water > max_water:
                    max_water = current_water

                while left < right and height[left] <= h_left:
                    left += 1
            else:
                current_water = h_right * (right - left)
                if current_water > max_water:
                    max_water = current_water

                while left < right and height[right] <= h_right:
                    right -= 1
                    
        return max_water