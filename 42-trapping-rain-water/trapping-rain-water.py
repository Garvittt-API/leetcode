class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                # Only calculate if current height is less than the max
                if height[left] < left_max:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
        return water