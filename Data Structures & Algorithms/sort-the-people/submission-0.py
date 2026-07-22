class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic=list(zip(names,heights))
        final=[]
        dic.sort(key=lambda x: x[1], reverse=True)

        for key,value in dic:
            final.append(key)
        return final




        