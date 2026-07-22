class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1
        result = 0
        while j < len(s):
            result += abs(ord(s[j]) - ord(s[i]))
            i += 1
            j += 1
        return result