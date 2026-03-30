class MinStack:

    def __init__(self):
        self.stack_list=[]
        self.minimum=0
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        self.minimum=min(self.minimum,val)
        

    def pop(self) -> None:
        self.stack_list.pop()
        

    def top(self) -> int:
        if len(self.stack_list) > 0:
            return self.stack_list[-1]
        else:
            return None
        

    def getMin(self) -> int:
        return min(self.stack_list)
        
