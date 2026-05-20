class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char =='(' or char=='{' or char=='[':
                stack.append(char)
            elif ((len(stack)>0) and ((char==')' and stack[-1]=='(') or (char==']' and  stack[-1]=='[') or (char=='}' and stack[-1]=='{'))):
                stack.pop()
            else:
                stack.append(char)
        if len(stack)>0:
            return False
        else:
            return True

        