class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        l=[]
        for i in range(len(strs)):
            a=sorted(strs[i])
            a=''.join(a)
            print(a)
            if a not in hashmap:
                hashmap[a]=[]
            hashmap[a].append(strs[i])
        print(hashmap.values())
        return  list(hashmap.values())

            


     
        