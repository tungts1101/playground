"""Search a 2D matrix
Given a matrix with size m*n of integers. This matrix has the following properties:
    - Integers in each row are sorted from left to right.
    - The first integer of each row is greater than the last integer of the previous row.

Output a single boolean indicates whether the target exists in the matrix or not.

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 100
    - -10^4 <= matrix[i][j], target <= 10^4
"""

"""
Doing a 2-dimension binary search.
Firstly, find a row in which the target will belong to. The value of the target is
in between the first and the last values of this row.
Secondly, check if the target exists in this row.

Memory: O(1).
Time: O(log(mn) * log(n)) - O(log(mn)) for searching row and O(log(n)) for checking 
target in this row.
"""


class Solution:
    def searchRow(self, row: List[int], target: int) -> bool:
        lo = 0
        hi = len(row)

        while lo < hi:
            mi = (lo + hi) // 2
            if target == row[mi]:
                return True
            elif target < row[mi]:
                hi = mi
            else:
                lo = mi + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)

        while lo < hi:
            mi = (lo + hi) // 2
            row = matrix[mi]
            if row[0] <= target and target <= row[-1]:
                return self.searchRow(row, target)
            elif target < row[0]:
                hi = mi
            else:
                lo = mi + 1

        return False
