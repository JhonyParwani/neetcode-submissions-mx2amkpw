class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        n=len(height)
        prev_result=n*[0]
        next_result=n*[0]
        prev_stack=[]
        next_stack=[]
        for i in range(n-1,-1,-1):
            while next_stack and height[i]<=height[next_stack[-1]]:
                next_stack.pop()
            if len(next_stack)==0:
                next_result[i]=n
            else:
                next_result[i]=next_stack[-1]
            next_stack.append(i)
        for i in range(n):
            while prev_stack and height[i]<=height[prev_stack[-1]]:
                prev_stack.pop()
            if len(prev_stack)==0:
                prev_result[i]=-1
            else:
                prev_result[i]=prev_stack[-1]
            prev_stack.append(i)
        area=[0]*n
        for i in range(n):
            area[i]=height[i]*(next_result[i]-prev_result[i]-1)
        max_area=0
        for a in area:
            max_area=max(max_area,a)
        print(next_result)
        print(prev_result)
        print(area)
        return max_area


        