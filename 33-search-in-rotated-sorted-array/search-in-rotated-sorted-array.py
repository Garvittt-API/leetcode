class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) >> 1  # Bitwise shift is sometimes faster
            mid_val = nums[mid]
            
            if mid_val == target:
                return mid
            
            # Use direct comparison against bounds
            if nums[low] <= mid_val:
                if nums[low] <= target < mid_val:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if mid_val < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1