class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack) if self.stack else None