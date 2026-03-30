class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp=[]
        for i in range(len(tokens)):
            if tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='*' or tokens[i]=='/':
                    total=0
                    digit1=int(temp.pop())
                    digit2=int(temp.pop())
                    if tokens[i]=='+':
                        total=digit1 + digit2
                    if tokens[i]=='-':
                        total=digit2 - digit1
                    if tokens[i]=='*':
                        total=digit1 * digit2
                    if tokens[i]=='/':
                        total=int(digit2 / digit1)
                    temp.append(total)
            else:
                temp.append(tokens[i])
        print(temp)
        return int(temp[0])
            
        