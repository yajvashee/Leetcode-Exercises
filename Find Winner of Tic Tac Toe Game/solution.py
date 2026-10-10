class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        a_moves = set()
        b_moves = set()
        winning_moves = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
        for index,move in enumerate(moves):
            if index %2 == 0:
                a_moves.add(3*move[0] + move[1] + 1)
                for wm in winning_moves:
                    if set(wm).issubset(a_moves):
                        return 'A'
            else:
                b_moves.add(3*move[0] + move[1] + 1)
                for wm in winning_moves:
                    if set(wm).issubset(b_moves):
                        return 'B'
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
