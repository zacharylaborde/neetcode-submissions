class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}

        # Create a dictionary that tells us the number of occurrences of each character there is in a word
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        # Check for two keys that have odd numbers next to them. If true, return false. Else, return true. 
        odd_numbers = 0
        for v in d.values():
            if v % 2 == 1:  # Is this number odd? 
                odd_numbers += 1
            if odd_numbers > 1:
                return False
        
        return True
