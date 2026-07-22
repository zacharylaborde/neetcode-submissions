class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # Declare variables.
        total_shift = 0
        
        # Compute the total shift.
        for command in shift:
            total_shift += command[1] if command[0] == 1 else -command[1]
        total_shift %= len(s)
        
        # Perform the shift.
        return s[-total_shift:] + s[:-total_shift]  

        