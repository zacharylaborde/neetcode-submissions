class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        d = {}

        # Combine and sort all arrays.

        sorted_array = []
        for array in arrays:
            sorted_array.append(array[0])
            sorted_array.append(array[-1])
        sorted_array = sorted(sorted_array)

        # Get dictionary containing numbers with their matching indicies.
        i = 0
        while i < len(arrays):
            if arrays[i][0] in d:
                d[arrays[i][0]].append(i)
            else:
                d[arrays[i][0]] = [i]
            if arrays[i][-1] in d:
                d[arrays[i][-1]].append(i)
            else:
                d[arrays[i][-1]] = [i]
            i += 1

        # Get the largest numbers without matching indicies
        ptr_l = 0
        ptr_r = -1
        while len(d[sorted_array[ptr_l]]) == 1 and d[sorted_array[ptr_l]] == d[sorted_array[ptr_r]]:
            # Move the ptrs closer together
            if sorted_array[ptr_l + 1] - sorted_array[ptr_l] > sorted_array[ptr_r] - sorted_array[ptr_r - 1]:
                ptr_r -= 1
            else:
                ptr_l += 1

        return abs(sorted_array[ptr_r] - sorted_array[ptr_l])