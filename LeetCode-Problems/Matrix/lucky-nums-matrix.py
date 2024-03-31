class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        """
        Given an m x n matrix of distinct numbers,
        find all lucky numbers in the matrix.

        A lucky number is an element of the matrix such that
        it is the minimum element in its row and maximum in its column.

        Constraints:
            - All elements in the matrix must be distinct.
            - 1 <= matrix[i][j] <= 10^5
        """
        greatest_in_col = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            min_element_col_idx = matrix[i].index(row_min)
            for j in range(len(matrix)):
                greatest_in_col.append(matrix[j][min_element_col_idx])
            if row_min == max(greatest_in_col):
                return [row_min]
            else:
                greatest_in_col.clear()


if __name__ == "__main__":
    sol = Solution()
    m1 = [[3,7,8],[9,11,13],[15,16,17]]
    m2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(sol.luckyNumbers(m1))
    print(sol.luckyNumbers(m2))