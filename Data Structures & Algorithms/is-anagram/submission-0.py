class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = [{}, {}]
        for i, l in enumerate([s, t]):
            for c in l:
                if c in ds[i]:
                    ds[i][c] += 1
                else:
                    ds[i][c] = 1
        if ds[0] == ds[1]:
            return True
        return False
        


        