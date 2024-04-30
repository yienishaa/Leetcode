import sys
class MinStack:

    def __init__(self):
        self.l = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.l.append(val)
        minv = min(val, self.min_val[-1] if self.min_val else val) #if min_val is not empty use min_val[-1], if not use val to 
                                                            # compare with val
                                                            # either val,min_val[-1] or val, val is used in the min      
                                                            # function to compare
        self.min_val.append(minv)

    def pop(self) -> None:
        self.l.pop(-1)
        self.min_val.pop(-1)

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
