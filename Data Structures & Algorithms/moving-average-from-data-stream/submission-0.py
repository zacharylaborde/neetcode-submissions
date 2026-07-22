class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.window_size = size
        

    def next(self, val: int) -> float:
        if len(self.window) >= self.window_size:
            self.window.pop(0)
        
        self.window.append(val)

        average = 0
        for v in self.window:
            average += v
        average /= len(self.window)

        return average

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
