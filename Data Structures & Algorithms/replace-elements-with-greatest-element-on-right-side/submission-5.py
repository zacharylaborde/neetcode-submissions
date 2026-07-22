class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range (len(arr) -1, -1, -1):
            if arr[i] > largest:
                arr[i], largest = largest, arr[i]
            else:
                arr[i] = largest
        return arr