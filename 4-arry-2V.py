# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, matrix, rows, columns, number):
        # write code here
        found = False

        if matrix is not None and rows > 0 and columns > 0:
            row = 0
            column = columns - 1
            while row < rows and column >= 0:
                if matrix[row][column] == number:
                    found = True
                    break
                elif matrix[row][column] > number:
                    column -= 1
                else:
                    row += 1

        return found


if __name__ == '__main__':
    matrix = [[1, 2, 8, 9],
              [2, 4, 9, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15]]
    s = Solution()
    print s.Find(matrix, 4, 4, 7)
