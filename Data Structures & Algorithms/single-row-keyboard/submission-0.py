class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dict = {}

        for i, key in enumerate(keyboard):
            keyboard_dict[key] = i

        curr_position = 0
        total_distance = 0
        for c in word:
            prev_position = curr_position
            curr_position = keyboard_dict[c]
            total_distance += abs(curr_position - prev_position)
        
        return total_distance

        