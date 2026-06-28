class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the list
        results = []
        
        for i in range(len(nums)):
            # Step 2: Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            # Step 3: Use two pointers to find the other two numbers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return results

# How to test your code:
my_list = [-1, 0, 1, 2, -1, -4]
solver = Solution()
print(solver.threeSum(my_list))