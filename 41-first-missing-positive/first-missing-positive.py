class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # Cache nums[i] to avoid repeated list lookups
            val = nums[i]
            # Use a while loop to place the value in its correct position
            while 1 <= val <= n and nums[val - 1] != val:
                # Perform the swap directly
                nums[val - 1], nums[i] = val, nums[val - 1]
                # Update val to the new value that was swapped into index i
                val = nums[i]
                
        # Final pass to find the first index mismatch
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1