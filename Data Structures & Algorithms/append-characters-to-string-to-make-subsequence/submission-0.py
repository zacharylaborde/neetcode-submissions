class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Figure out if t is a substring of s or how far away it is from being a substring of s
        if t == "":
            return 0

        # Set variables
        i = 0
        
        # Algorithm
        for c in s:
            if c == t[i]:
                i += 1
            if i >= len(t):
                return 0
            
        # i is now some number.
        return len(t) - i