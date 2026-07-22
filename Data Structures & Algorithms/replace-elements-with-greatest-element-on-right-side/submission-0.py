class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i, n in enumerate(arr[::-1]):
            arr[-i - 1] = largest
            largest = max(largest, n) 
        return arr