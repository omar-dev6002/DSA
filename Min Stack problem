class MinStack:

    def __init__(self):
        self.stack = []
        # Each element is a tuple: (value, current_min)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1]
            self.stack.append((val, current_min))     

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        raise IndexError("top from empty stack")

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("getMin from empty stack")
