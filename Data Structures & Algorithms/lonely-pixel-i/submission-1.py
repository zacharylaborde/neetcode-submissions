class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # First find the sizes of m and n.
        number_of_lonely_black_pixels = 0

        # Iterate through each row (n). 
        # If a row has exactly one black pixel, add the column of that black pixel to columns_to_check.
        columns_to_check = []
        for r in picture:
            number_of_black_pixels = 0
            column = None
            for i, c in enumerate(r):
                if c == "B":
                    number_of_black_pixels += 1
                    column = i
                if number_of_black_pixels >= 2:
                    column = None
                    break
            if not column is None:
                columns_to_check.append(column)


        # Iterate through columns_to_check's columns in our matrix.
        for c in columns_to_check:
            number_of_black_pixels = 0
            for i in range(len(picture)):
                if picture[i][c] == "B":
                    number_of_black_pixels += 1
            if number_of_black_pixels == 1:
                number_of_lonely_black_pixels += 1

        return number_of_lonely_black_pixels
