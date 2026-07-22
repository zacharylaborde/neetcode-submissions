class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        confusing = {0, 1, 6, 8, 9}
        s = str(n)
        new_s = ""

        for c in s[::-1]:
            if not int(c) in confusing:
                return False
            new_s += str(flip[int(c)])
        print(new_s)
        if int(new_s) != int(s):
            return True
        else:
            return False