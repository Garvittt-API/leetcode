class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Cyclic Sort: Place each number x at index x-1 if 1 <= x <= n
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap nums[i] with the element at its target position
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        # 2. Identify the first index where the value is not i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 3. If all indices match, the missing number is n + 1
        return n + 1