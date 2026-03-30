class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap={}
        for i in range(len(position)):
            for j in range(len(speed)):
                if i==j:
                    hashmap[position[i]]=speed[j]
        sort_postion=sorted(position,reverse=True)
        print(hashmap)
        time=[]
        for pos in sort_postion:
            print(pos,hashmap[pos])
            time.append((target-pos)/hashmap[pos])
        print(time)
        stack=[]
        time.reverse()
        print(time)
        while len(time) !=0:
            temp=time.pop()
            if len(stack) and stack[-1]>=temp:
                pass
            else:
                stack.append(temp)
        return len(stack)

        

         
        