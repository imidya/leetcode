class Solution(object):
    def is_ship(self, i, j):
        if self.board[i][j] == 'X':
            return True
        else:
            return False

    def mark_ship(self, i, j):
        self.board[i][j] = '1'
        if i + 1 < len(self.board) and self.is_ship(i + 1, j):
            self.mark_ship(i + 1, j)
        elif j + 1 < len(self.board[0]) and self.is_ship(i, j + 1):
            self.mark_ship(i, j + 1)

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.board = board
        self.count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.is_ship(i, j):
                    self.count += 1
                    self.mark_ship(i, j)

        return self.count


if __name__ == '__main__':
    s = Solution()
    board = [
        ['X', '.', '.', 'X'],
        ['X', '.', '.', 'X'],
        ['.', '.', '.', 'X']
    ]
    print(s.countBattleships(board))
