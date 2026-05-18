class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        list1=[]
        final=[]
        hashmap=defaultdict(list)
        for s in strs:
            sorted_s="".join(sorted(s))
            if sorted_s in hashmap:
                list1=hashmap[sorted_s]
                list1.append(s)
                hashmap[sorted_s]=list1

                
            else:
                hashmap[sorted_s]=[s]
        print(hashmap)
        for key,value in hashmap.items():
            final.append(hashmap[key])
        return final

            

    