class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        count = 0

        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for k, v in d.items():
            if k + 1 in d:
                count += v
        
        return count