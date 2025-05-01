
# Problem Statement

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

# Solution


from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        # Track seen numbers in each row, column, and 3x3 grid
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)  # Key = (row//3, col//3)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue  # Skip empty cells

                # Check if the number already exists in the row, column, or grid
                if (
                        num in rows[r] or
                        num in cols[c] or
                        num in grids[(r // 3, c // 3)]
                ):
                    return False  # Violation of Sudoku rule

                # Add the number to the respective row, column, and grid
                rows[r].add(num)
                cols[c].add(num)
                grids[(r // 3, c // 3)].add(num)

        return True  # No violations found


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    solution = Solution()
    print(solution.isValidSudoku(board))
