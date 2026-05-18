class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter 
        final=Counter(nums)
        print(final)
        heap=[]
        for key,value in final.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        list1=[]
        for key,value in heap:
            list1.append(value)
        return list1
            
        