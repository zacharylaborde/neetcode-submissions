class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            s = set()

            # Crush.
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == 0:
                        continue

                    if row+2 < len(board) and board[row][col] == board[row + 1][col] and board[row][col] == board[row + 2][col]:
                        s.add((row, col))
                        s.add((row+1, col))
                        s.add((row+2, col))
                
                    if col+2 < len(board[0]) and board[row][col] == board[row][col+1] and board[row][col] == board[row][col+2]:
                        s.add((row, col))
                        s.add((row, col+1))
                        s.add((row, col+2))
        
            if len(s) == 0:
                break
        
            for i in s:
                board[i[0]][i[1]] = 0

            # Gravity
            for col in range(len(board[0])-1, -1, -1):
                new_col = []
                for row in range(len(board)):
                    if board[row][col] != 0:
                        new_col.append(board[row][col])
            
                for row in range(len(board)-1, -1, -1):
                    if len(new_col) > 0:
                        board[row][col] = new_col.pop()
                    else:
                        board[row][col] = 0
        return board