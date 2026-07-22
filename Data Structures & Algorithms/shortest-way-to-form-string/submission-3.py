class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        laps = 0
        last_meaningful_lap = 0
        j = 0

        while j < len(target):
            
            if source[i] == target[j]:
                j += 1
                last_meaningful_lap = laps
            
            if laps - last_meaningful_lap >= 2: # Current character is not in the source string
                return -1

            i = (i + 1) % len(source)
            if i == 0:
                laps += 1
        
        if i > 0:
            laps += 1
        
        return laps