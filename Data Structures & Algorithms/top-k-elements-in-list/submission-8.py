class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        final_list=[]
        import heapq
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for key,value in hashmap.items():
            heapq.heappush(final_list,[value,key])
        print(final_list)

        while len(final_list)>k:
            heapq.heappop(final_list)
        final=[]
        print(final_list)
        for key,value in final_list:
            final.append(value)
        return final
        