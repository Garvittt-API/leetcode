class Solution:
    def jump(self, nums: list[int]) -> int:
        # If there's only 1 element, we are already at the destination
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_window_end = 0
        farthest_reachable = 0
        
        # We don't need to process the last element because once 
        # current_window_end reaches or exceeds it, we are done.
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current spot
            farthest_reachable = max(farthest_reachable, i + nums[i])
            
            # If we've reached the end of our current jump's range
            if i == current_window_end:
                jumps += 1                  # We must take a jump
                current_window_end = farthest_reachable  # Extend our window
                
                # Optimization: If our new window can already reach the end, stop early
                if current_window_end >= len(nums) - 1:
                    break
                    
        return jumps