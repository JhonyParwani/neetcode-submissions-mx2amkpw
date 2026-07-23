class Solution:




    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        to_move=0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    temp=arr1[j]
                    arr1[j]=arr1[to_move]
                    arr1[to_move]=temp
                    to_move+=1
        arr1[to_move:]=sorted(arr1[to_move:len(arr1)])
        return arr1



        