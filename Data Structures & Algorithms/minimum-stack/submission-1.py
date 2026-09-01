class MinStack:

    def __init__(self):
        self.stack_min = []

    def push(self, val: int) -> None:
        if len(self.stack_min) == 0:
            min_value = val
        else:
            min_value = min(val, self.stack_min[-1][1])
        self.stack_min.append((val,min_value))
        

    def pop(self) -> None:
        value, min_val = self.stack_min.pop()
        return value

    def top(self) -> int:
        value, min_val = self.stack_min[-1]
        return value
        

    def getMin(self) -> int:
        value, min_val = self.stack_min[-1]
        return min_val
