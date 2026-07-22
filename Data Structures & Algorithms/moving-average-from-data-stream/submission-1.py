class MovingAverage:
    class Queue:
        class Node:
            def __init__(self):
                self.v = None
                self.n = None
        
        def __init__(self, max_size: int):
            self.max_size = max_size
            self.head = self.Node()
            self.tail = self.head
            self.length = 0

        def add(self, v):
            if self.length == self.max_size:
                self.head = self.head.n
            else:
                self.length += 1

            self.tail.v = v
            self.tail.n = self.Node()
            self.tail = self.tail.n
        
        def average(self):
            ptr = self.head
            average = 0
            while ptr.v != None:
                average += ptr.v
                ptr = ptr.n
            average /= self.length
            return average

    def __init__(self, size: int):
        self.window = self.Queue(size)

    def next(self, val: int) -> float:        
        self.window.add(val)
        return self.window.average()

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
