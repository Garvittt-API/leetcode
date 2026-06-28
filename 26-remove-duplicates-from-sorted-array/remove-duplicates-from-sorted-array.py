class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write_ptr = 1
        
        for read_ptr in range(1, len(nums)):
            if nums[read_ptr] != nums[read_ptr - 1]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1

        return write_ptr