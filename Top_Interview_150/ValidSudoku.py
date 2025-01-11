"""
Problem: Valid Sudoku

Objective:
- Given a partially filled 9x9 Sudoku board, determine if it is a valid Sudoku board.
- A valid Sudoku board means:
  1. Each row must contain digits 1-9 without repetition.
  2. Each column must contain digits 1-9 without repetition.
  3. Each of the nine 3x3 subgrids must also contain digits 1-9 without repetition.
  4. The empty cells are represented by '.'.

Approach:
- The solution uses three sets to track the numbers seen in each row, column, and 3x3 subgrid. 
- If a number is encountered in any of these sets while processing the board, it indicates a repetition, and the board is invalid.
- We use the properties of the Sudoku board (fixed size of 9x9) to check the validity efficiently.

Algorithm:
1. **Initialize Sets:**
   - Create three lists (`rowSet`, `colSet`, and `boxSet`), each containing 9 empty sets. These sets will track the numbers seen in each row, column, and 3x3 subgrid, respectively.
   
2. **Iterate Through the Board:**
   - Loop through the board with two nested loops, `i` for rows (0 to 8) and `j` for columns (0 to 8).
   
3. **Check for Valid Numbers:**
   - For each cell on the board, if the value is not '.', then:
     - Calculate the index of the corresponding 3x3 subgrid using the formula `box_index = (i//3)*3 + (j//3)`.
     - Check if the number is already present in the corresponding row, column, or subgrid set. If it is, return `False` because the board is invalid.
     - If the number is not found in any set, add it to the corresponding row, column, and subgrid sets.
   
4. **Return True:**
   - If the loops complete without finding any duplicates, return `True`, indicating that the board is valid.

Time Complexity:
- **Nested Loops:** We iterate through the 9x9 grid once, which takes O(81) time (constant time due to the fixed size).
- **Set Operations (Insertion and Lookup):** O(1) on average, as adding and checking for membership in a set takes constant time.
- **Overall Time Complexity:** O(1) due to the fixed size of the board (9x9 grid). While this is constant, in larger grids, the time complexity would scale linearly with the number of cells.

Space Complexity:
- **Space for Sets:** We use three lists (`rowSet`, `colSet`, and `boxSet`), each containing 9 sets. This gives a space complexity of O(9), which is constant due to the fixed size.
- **Overall Space Complexity:** O(1), as the space used does not depend on the input size.

Edge Cases:
- A fully filled board: The algorithm works for fully filled boards as well as partially filled boards.
- Empty cells: Empty cells represented by '.' are ignored during the check.
- Invalid boards: If there are any duplicate numbers in rows, columns, or subgrids, the function will return `False`.

Example:
Input:
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output:
True

Explanation:
- The board is valid because there are no duplicates in any row, column, or 3x3 subgrid.

Input:
board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output:
False

Explanation:
- The board is invalid because the number '8' is repeated in the first and fourth rows.

Code:
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_index = (i//3)*3 + (j//3)

                    if num in rowSet[i] or num in colSet[j] or num in boxSet[box_index]:
                        return False

                    rowSet[i].add(num)
                    colSet[j].add(num)
                    boxSet[box_index].add(num)

        return True


                
