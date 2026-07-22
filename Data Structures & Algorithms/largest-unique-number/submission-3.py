class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            if not n in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for n in sorted(d.keys())[::-1]:
            if d[n] == 1:
                return n
        
        return -1