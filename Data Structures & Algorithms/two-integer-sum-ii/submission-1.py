class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        first=0
        last=n-1
        while first!=last:
            if numbers[first]+numbers[last]>target:
                last-=1
            elif numbers[first]+numbers[last]<target:
                first+=1
            else:
                return [first+1,last+1]
