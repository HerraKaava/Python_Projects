class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Given a 2D integer array 'matrix', finds the transpose of 'matrix'
        (without using functions like NumPy's numpy.ndarray.T).

        The transpose of a matrix is the matrix flipped over its main diagonal,
        switching the matrix's row and column indices.
        """
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

        # len(matrix) stands for the number of rows in matrix
        #  This is because matrix is a list of lists, where each inner list represents a row.

        # len(matrix[0]) stands for the number of columns in a matrix
        # This is based on the assumption that all rows in the matrix have the same number of elements
        # (which is a standard property of a matrix).


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.transpose(matrix))


