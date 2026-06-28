class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_ptr = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_ptr] = nums[i]
                write_ptr += 1

        return write_ptr