class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = nums
        

    def showFirstUnique(self) -> int:
        first_unique = -1
        checked = set()
        for i, n in enumerate(self.queue):
            
            if n in checked:
                continue
            else:
                checked.add(n)

            if i < len(self.queue) and not n in self.queue[i+1:]:
                first_unique = n
                break
        return first_unique


    def add(self, value: int) -> None:
        self.queue.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
