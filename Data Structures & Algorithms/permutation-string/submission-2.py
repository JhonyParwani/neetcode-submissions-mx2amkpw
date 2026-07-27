class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start=0
        from collections import Counter
        counts1=Counter(s1)
        for j in range(len(s1)-1,len(s2)):
            # print("".join(s1),s2[start:j+1])
            counts2=Counter(s2[start:j+1])

            if counts1==counts2:
                return True
            start+=1
        return False
            
                
                



        