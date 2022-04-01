"""Maximal rectangle
Given rows*cols binary matrix. Find the largest area of rectangle filled with 1.
Example:
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
The largest rectangle is [(1,2), (2,4)] with area of 6.

Output a single number indicates the maximal rectangle area in the matrix.

Constraints:
    - 1 <= rows, cols <= 200.
    - matrix[i][j] is either 0 or 1.
"""

"""
Reference: https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/?ref=lbp
A subroutine which calculates the maximal area of histogram will be borrowed for this task.
We will not cover any detail of this subroutine in here since it need another post to explain.
Assume we have that subroutine, now we need to create a histogram from original matrix. We will 
build up the bars of histogram by looping through each row of the matrix. If we meet 1, the bar 
will get higher, and if we meed 0, the bar will be squashed out.
Take the example matrix, we will have these histogram:
Row 1: 1 0 1 0 0 --> maximal area is 1.
Row 2: 2 0 2 1 1 --> maximal area is 2.
Row 3: 3 1 3 2 2 --> maximal area is 6.
Row 4: 4 0 0 3 0 --> maximal area is 6.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def max_area_histogram(histogram):
            """This function calculates maximum rectangular area
            under given histogram with n bars
            
            Args:
                histogram (list): A list of bars.
            
            Returns:
                int: Maximum rectangular area.
            """
            # A stack to store indexes of histogram.
            # The bars stored in the stack is always in increasing order
            # of their heights.
            stack = []
            max_area = 0
            index = 0
            while index < len(histogram):
                # If the stack is empty or current bar is higher than
                # the top bar in the stack, push index to stack.
                if not stack or histogram[stack[-1]] <= histogram[index]:
                    stack.append(index)
                    index += 1
                # If current bar is lower than the top bar in the stack,
                # calculate rectangular area with the top bar as the smallest. 
                # Right index is the index, and left index is the index of
                # previous item in the stack.
                # The area will be calculated as:
                #   a = height(top_stack) * (right_index - left_index - 1)
                else:
                    top_stack = stack.pop()
                    area = histogram[top_stack] * ((index - stack[-1] - 1) if stack else index)
                    max_area = max(max_area, area)
            
            # Pop out the remaining bar until stack is empty
            while stack:
                top_stack = stack.pop()
                area = histogram[top_stack] * ((index - stack[-1] - 1) if stack else index)
                max_area = max(max_area, area)
            
            return max_area
        
        # Constructing a histogram while looping through each row.
        max_area = 0
        histogram = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            histogram = [histogram[i] + int(row[i]) if int(row[i]) == 1 else 0 for i in range(len(histogram))]
            max_area = max(max_area, max_area_histogram(histogram))
        
        return max_area