class Solution:
    def isValid(self, temp: str) -> bool:
        stack=[]
        if temp is  None:
            return True
        for i in range(len(temp)):
            if len(stack)>0 and stack[-1]=='[' and temp[i]==']' or len(stack)>0 and stack[-1]=='{' and temp[i]=='}' or len(stack)>0 and stack[-1]=='(' and temp[i]==')':
                stack.pop()    
            elif temp[i]=='[' or temp[i]=='(' or temp[i]=='{':
                stack.append(temp[i])
            else:
                return False 
        if len(stack)>0:
            return False
        else:
            return True
        