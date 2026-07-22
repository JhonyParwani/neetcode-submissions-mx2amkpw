class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        final=""
        find=-1
        for i in s:
            for j in range(find+1,len(t)):
                if i==t[j]:
                    final+=i
                    find=j
                    break
        if final==s:
            return True
        else:
            return False

                

                

        

                    
                    

        
        