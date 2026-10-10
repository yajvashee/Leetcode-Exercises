# 1275.Find Winner of Tic Tac Toe Game

## Problem
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
Example 2:


Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
Example 3:


Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.

## Approach
1. Created sets called a_moves and b_moves to track moves by a and b.
2. Created a list of sets which contained the list winning combinations.
3. For each move made.
4. If it was an odd number move(1st,3rd,5th etc), this would be a move made by a.
5. I would calculate which box A made their move by doing 3* row number + column number.
6. I would add that value to the set containing a list of A moves.
7. If after that move one of the winning combinations is a subset of A moves, then I would return that A has won the game.
8. I used the same principle for B.
9. Once going through all the moves, if the number of moves made is 9, the game has finished and I would return the outcome as a Draw.
10. If the number of moves is less than 9, then the game is still going on so I would return Pending.