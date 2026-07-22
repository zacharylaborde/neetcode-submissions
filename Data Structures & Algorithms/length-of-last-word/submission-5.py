class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while i > -1:
            if s[i] != " ":
                count += 1
            elif count > 0:
                return count
            i -= 1
        return count