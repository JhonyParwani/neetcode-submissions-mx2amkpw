class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter,defaultdict 
        start=0
        end=0
        hashmap2=Counter(t)
        hashmap={}
        mini=float('inf')
        result=""
        while end<len(s):
            if s[end] in hashmap:
                hashmap[s[end]]+=1
            else:
                hashmap[s[end]]=1
            is_valid=True
            for c in hashmap2:
                if hashmap.get(c,0)<hashmap2[c]:
                    is_valid=False
                    break
            while is_valid:
                is_valid=True
                for c in hashmap2:
                    if hashmap.get(c,0)<hashmap2[c]:
                        is_valid=False
                        break
                if is_valid==False:
                    break
                if len(s[start:end+1])<mini:
                    
                    mini = len(s[start:end+1])   

                    result = s[start:end+1]
                hashmap[s[start]]-=1
                if hashmap[s[start]]==0:
                    del hashmap[s[start]]
                start+=1  
            end+=1
        return result
            

        