class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end=len(s)-1
        start=0
        for  i in range(len(s)//2):
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            end-=1
            start+=1
        
            
        
        