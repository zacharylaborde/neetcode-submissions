class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        polarity = len(s) - len(t)

        # Special simple cases
        # If abs(ploarity) is 2 or more, edit distance must be 2 or more. 
        if abs(polarity) > 1:
            return False

        if len(s) == 0 and len(t) == 0:
            return False
        
        if len(s) == 0 or len(t) == 0:
            return True
        
        # Check if there is exactly ONE replacement.
        if polarity == 0:
            differences = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    differences += 1
            return differences == 1

        # Delete Logic
        if polarity < 0: # len(t) > len(s)
            differences = 0
            for i in range(len(s)):
                while t[i+differences] != s[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences <= 1

        if polarity > 0: # len(s) > len(t)
            differences = 0
            for i in range(len(t)):
                while s[i+differences] != t[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences <= 1

