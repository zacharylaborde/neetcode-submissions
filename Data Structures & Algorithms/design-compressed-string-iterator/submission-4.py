class StringIterator:

    def __init__(self, compressedString: str):
        self.ll = []
        curr = 0

        i = 0
        while i < len(compressedString):
            currentCharacter = ""
            currentDigit = ""
            while not compressedString[i].isdigit():
                currentCharacter += compressedString[i]
                i += 1
                        
            while compressedString[i].isdigit():
                currentDigit += compressedString[i]
                i += 1
                if i >= len(compressedString):
                    break
            
            self.ll.append([currentCharacter, int(currentDigit)])

    def next(self) -> str:
        val = None
        if self.hasNext():
            val = self.ll[0][0]
            self.ll[0][1] -= 1
            if self.ll[0][1] == 0:
                self.ll.pop(0)
        print(val)
        return val
            


    def hasNext(self) -> bool:
        return len(self.ll) > 0
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
