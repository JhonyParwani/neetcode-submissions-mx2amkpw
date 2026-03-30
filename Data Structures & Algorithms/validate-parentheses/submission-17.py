class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        my_list = list()
        if len(s) == 0:
            return True
        for i in range(len(s)):
            print(s[i])

            
            if (len(temp) !=0 and temp[-1]=='{' and s[i]=='}') or (len(temp) !=0 and temp[-1]=='[' and s[i]==']') or (len(temp) !=0 and temp[-1]=='(' and s[i]==')'):

                temp.pop()
                print(temp)
            else:
                if (s[i]=='[' or s[i]=='{' or s[i]=='('):
                    temp.append(s[i])
                    print(temp)
                else:
                    return False
        if len(temp)==0:
            return True 
        else:
            return False
