class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=len(temperatures)*[0]
        stack=[]
        last_index=len(temperatures) -1 
        for i,temp in enumerate(reversed(temperatures)):
            index=last_index-i
            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                result[index]=0
            else:
                result[index]=stack[-1] - index
            stack.append(index)
            
        return result
        