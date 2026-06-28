class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        write_ptr = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[write_ptr] = nums[i]
                write_ptr += 1
                
        return write_ptr