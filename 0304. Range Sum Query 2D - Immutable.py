
# Problem Statement

"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the
rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""


# Solution


class NumMatrix:

    def __init__(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        # Create a prefix sum matrix with one extra row and column (for easier calculations)
        self.prefix = [[0] * (col + 1) for _ in range(row + 1)]

        # Build the prefix sum matrix
        for i in range(row):
            for j in range(col):
                # Formula:
                # Current cell = original value + left + top - top-left (to avoid double count)
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i + 1][j]      # left
                    + self.prefix[i][j + 1]      # top
                    - self.prefix[i][j]          # top-left
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Use inclusion-exclusion to get the sum of the submatrix
        # Sum = bottom-right - top-strip - left-strip + top-left-overlap
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


# Test the class
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
