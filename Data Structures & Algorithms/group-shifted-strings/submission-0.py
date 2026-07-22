class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}

        for string in strings:
            
            deltas = self.deltas(string)
            if deltas in d:
                d[deltas].append(string)
            else:
                d[deltas] = [string]
        
        return [v for v in d.values()]

    def deltas(self, s: str) -> str:
        deltas = ""

        i = 0
        while i < len(s) - 1:
            deltas += str((ord(s[i]) - ord(s[i+1])) % 26) + "."
            i += 1
        
        return deltas