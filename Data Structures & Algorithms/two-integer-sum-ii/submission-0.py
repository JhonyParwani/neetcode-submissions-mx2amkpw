class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        hashmap={}
        for i,num in enumerate(numbers):
            hashmap[num]=i
        first=0
        last=n-1
        while first!=last:
            if numbers[first]+numbers[last]>target:
                last-=1
            elif numbers[first]+numbers[last]<target:
                first+=1
            else:
                return [first+1,last+1]
