class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        lce = -1
        checked = set()
        sorted_array = []


        for l in mat:
            sorted_array += l
        
        sorted_array = sorted(sorted_array)

        for i in sorted_array:
            if i in checked:
                continue
            
            checked.add(i)
            in_all = True
            for l in mat:
                if not i in l:
                    in_all = False
                    break
            
            if in_all:
                lce = i
                break
        return lce



