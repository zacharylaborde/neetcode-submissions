class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # Check for winners
        for row in range(len(self.board)):
            streak = True
            for col in range(len(self.board)):
                if self.board[row][col] != player:
                    streak = False
                    break
            if streak:
                return player
        
        for col in range(len(self.board)):
            streak = True
            for row in range(len(self.board)):
                if self.board[row][col] != player:
                    streak = False
                    break
            if streak:
                return player
        
        streak = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                streak = False
                break
        if streak:
            return player
        
        streak = True
        for i in range(len(self.board)):
            if self.board[i][-1-i] != player:
                streak = False
                break

        if streak:
            return player
        
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
