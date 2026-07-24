class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        hashmap=Counter(nums)
        for key,value in hashmap.items():
            if value<2:
                return key
        