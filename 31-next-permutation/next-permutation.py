class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first index i such that nums[i] < nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            # Step 2: Find the first index j such that nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap elements
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 4: Reverse the sub-array from i + 1 to end
        nums[i + 1:] = reversed(nums[i + 1:])