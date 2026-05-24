class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        end=0
        from collections import defaultdict
        hashmap={}
        freq=0
        maxi=0
        while end<len(s):
            if s[end] in hashmap:
                hashmap[s[end]]+=1
            else:
                hashmap[s[end]]=1
            freq=max(hashmap.values())
            while ((end-start)+1) - freq>k:
                print((end-start)-freq)
                hashmap[s[start]]-=1
                start+=1
            maxi=max(end-start+1,maxi)
            end+=1
        return maxi
            
            



        

            
            
        