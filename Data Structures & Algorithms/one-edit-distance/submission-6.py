class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        polarity = len_s - len_t

        # Special simple cases
        # If abs(ploarity) is 2 or more, edit distance must be 2 or more. 
        if abs(polarity) > 1:
            return False

        if len_s == 0 and len_t == 0:
            return False
        
        if len_s == 0 or len_t == 0:
            return True
        
        # Check if there is exactly ONE replacement.
        if polarity == 0:
            differences = 0
            for i in range(len_s):
                if s[i] != t[i]:
                    differences += 1
            return differences == 1

        # Delete Logic
        if polarity < 0: # len(t) > len(s)
            differences = 0
            for i in range(len_s):
                while t[i+differences] != s[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences <= 1

        # Delete Logic
        if polarity > 0: # len(s) > len(t)
            differences = 0
            for i in range(len_t):
                while s[i+differences] != t[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences <= 1

