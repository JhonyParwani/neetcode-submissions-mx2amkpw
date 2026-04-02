class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start=0
        n=len(heights)
        end=n-1
        max_area=0
        while start < end:
            if heights[start] < heights[end]:
                max_area=max(max_area,((end-start)*min(heights[start],heights[end])))
                start+=1
            else:
                max_area=max(max_area,((end-start)*min(heights[start],heights[end])))
                end-=1
        return max_area



            

        