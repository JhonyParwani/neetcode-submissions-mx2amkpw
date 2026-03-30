class MinStack:

    def __init__(self):
        self.stack_list=[]
        self.min_stack_list=[]
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        if len(self.min_stack_list)>0 and val <=self.min_stack_list[-1]:
            self.min_stack_list.append(val)
        elif len(self.min_stack_list)==0:
            self.min_stack_list.append(val)
        print(self.stack_list)

    def pop(self) -> None:
        if len(self.stack_list)==0:
            return None 
        temp=self.stack_list.pop()
        if self.min_stack_list[-1] == temp:
            self.min_stack_list.pop()
        print('min stack is ',self.min_stack_list)
        print(self.stack_list)

        return temp


        

    def top(self) -> int:
        print(self.stack_list)

        return self.stack_list[-1]
        

    def getMin(self) -> int:
        print('min is ',self.min_stack_list[-1])
        return self.min_stack_list[-1]
        
