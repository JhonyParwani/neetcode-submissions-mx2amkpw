class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        hashmap=defaultdict(list)
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        print(hashmap)
        for key,value in hashmap.items():
            if value>1:
                return True 
        return False

        