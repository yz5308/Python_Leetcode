class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows == 1 or numRows >= len(s):
            return s

        zigzag = ['' for x in range(numRows)]

        row, step = 0, 1

        for crct in s:
            zigzag[row] += crct
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(zigzag)




        """
        # zigzag[row] row  step
        #   0          0     1
        #   1          1     1
        #   2          2    -1
        #   1          1    -1
        #   0          0     1

        Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

        Example 1:

        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

        Example 2:

        Input: "cbbd"
        Output: "bb"


        """
