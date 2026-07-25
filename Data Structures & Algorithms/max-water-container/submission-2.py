class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #two pointer 
        i, j=0, len(heights)-1
        maxWater=0
        # start the computation of every pair
        while i<j:
            #calculate the current water usage based on current value 
            waterUsage=(j-i)*min(heights[i], heights[j])
            maxWater=max(maxWater, waterUsage)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxWater