class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = 0
        mat3 = []

        for i in range(len(mat1)):        # rows of mat1 → rows of result
            mat3.append([])
            for j in range(len(mat2[0])): # cols of mat2 → cols of result
                result = 0
                for k in range(len(mat2)):  # cols of mat1 == rows of mat2
                    result += mat1[i][k] * mat2[k][j]
                mat3[i].append(result)
        
        return mat3
            