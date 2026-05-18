class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        hashmap=defaultdict(list)
        for i,num in enumerate(nums):
            diffrence=target-num
            if num in hashmap:
                print(hashmap)        
                return [hashmap[num],i]
            else:
                hashmap[diffrence]=i
        
