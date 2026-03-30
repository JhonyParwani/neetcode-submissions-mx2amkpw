class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        result_ns=[0]*n
        result_ps=[0]*n
        heights_reverse=heights[ : : -1]
        stack_ns=[]
        stack_ps=[]
        for i,h in enumerate(heights_reverse):
            start=n-i-1
            while stack_ns and h <= heights[stack_ns[-1]]:
                stack_ns.pop()
            if not stack_ns:
                result_ns[start]=n
            else:
                result_ns[start]=stack_ns[-1]
            stack_ns.append(start)
        print(result_ns)
        for start,h in enumerate(heights):
            while stack_ps and h <= heights[stack_ps[-1]]:
                stack_ps.pop()
            if not stack_ps:
                result_ps[start]=-1
            else:
                result_ps[start]=stack_ps[-1]
            stack_ps.append(start)
        print(result_ps)
        maxarea=0
        for i in range(len(heights)):
            a=result_ns[i]-result_ps[i] -1
            a=a*heights[i]
            maxarea=max(maxarea,a)
        return (maxarea)


            

        