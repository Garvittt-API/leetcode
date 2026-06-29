class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
            
        def find_bound(is_first: bool) -> int:
            low, high = 0, len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    bound = mid
                    # Narrow the search space depending on which bound we want
                    if is_first:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return bound
        
        # 1. Find the first occurrence
        first_pos = find_bound(True)
        
        # If target isn't found at all, we can exit early
        if first_pos == -1:
            return [-1, -1]
            
        # 2. Find the last occurrence
        last_pos = find_bound(False)
        
        return [first_pos, last_pos]