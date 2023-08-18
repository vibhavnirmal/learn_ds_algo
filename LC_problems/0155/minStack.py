# Remains unsolved ... 

class MinStack:
    def __init__(self):
        self.myList = []

    def push(self, val: int) -> None:
        self.myList.append(val)

    def pop(self) -> None:
        self.myList.remove()

    def top(self) -> int:
        self.myList[-1]

    def getMin(self) -> int:
        return min(self.myList)

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
    
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.pop(-3)
    obj.getMin()
    obj.pop()
    obj.top()
    obj.getMin()