class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0]+ nums[1]+nums[2]
        n = len(nums)
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                total = nums[i]+ nums[left] + nums[right]
                if abs (total-target)<abs(closest-target):
                    closest= total
                if total<target:
                    left+=1
                elif total>target:
                    right-=1
                else:
                    return total

        return closest