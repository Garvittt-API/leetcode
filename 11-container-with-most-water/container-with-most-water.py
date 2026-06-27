class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        curr_area=(end-start)*min(height[start],height[end])
        max_height=max(height)

        while start<end:
            curr_area=max(curr_area,((end-start)*min(height[start],height[end])))

            if curr_area > max_height*(end-start):
                return curr_area

            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return curr_area