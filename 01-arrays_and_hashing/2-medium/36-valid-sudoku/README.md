# Problem

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

>Note:\
>A Sudoku board (partially filled) could be valid but is not necessarily solvable.\
>Only the filled cells need to be validated according to the mentioned rules.

## Example 1:

> Input: board = \
> [["5","3",".",".","7",".",".",".","."]\
> ,["6",".",".","1","9","5",".",".","."]\
> ,[".","9","8",".",".",".",".","6","."]\
> ,["8",".",".",".","6",".",".",".","3"]\
> ,["4",".",".","8",".","3",".",".","1"]\
> ,["7",".",".",".","2",".",".",".","6"]\
> ,[".","6",".",".",".",".","2","8","."]\
> ,[".",".",".","4","1","9",".",".","5"]\
> ,[".",".",".",".","8",".",".","7","9"]]\
> Output: true

## Example 2:

> Input: board = \
> [["8","3",".",".","7",".",".",".","."]\
> ,["6",".",".","1","9","5",".",".","."]\
> ,[".","9","8",".",".",".",".","6","."]\
> ,["8",".",".",".","6",".",".",".","3"]\
> ,["4",".",".","8",".","3",".",".","1"]\
> ,["7",".",".",".","2",".",".",".","6"]\
> ,[".","6",".",".",".",".","2","8","."]\
> ,[".",".",".","4","1","9",".",".","5"]\
> ,[".",".",".",".","8",".",".","7","9"]]\
> Output: false\
> Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

## Constraints:

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

# Source

https://leetcode.com/problems/valid-sudoku/

# Solutions

## Brute Force

Let's start with a brute force solution. We can check each row, column, and sub-box by looping through the board and checking each element. We can use a set to keep track of the numbers we have seen so far. If we see a number that is already in the set, then the board is not valid. Otherwise, we add the number to the set and continue. If we reach the end of the board, then the board is valid.

## Optimized using Sets

We can optimize the brute force solution by using a set for each row, column, and sub-box. We can loop through the board and check each element. If we see a number that is already in the set for the row, column, or sub-box, then the board is not valid. Otherwise, we add the number to the set and continue. If we reach the end of the board, then the board is valid.
