class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        final=[]
        for i in words[0]:
            found=True
            for j in words[1:]:
                if i in j:
                    found=True
                else:
                    found=False
                    break
            if found==True:
                final.append(i)
                for k in range(1,len(words)):
                    words[k]=words[k].replace(i,"",1)                    
        return final

        