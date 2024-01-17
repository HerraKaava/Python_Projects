class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """
        Reshape the given m x n matrix 'mat'.
        The reshaping is done based on the parameters 'r' and 'c',
        which stand for rows and columns, respectively.

        The reshaped matrix will contain all the elements from the original matrix
        in the same row-traversing order as they were.

        If the reshape operation with the given parameters is possible and legal,
        the output will be the new reshaped matrix;
        Otherwise, the output will be the original matrix.

        Examples:
            Input: mat = [[1,2],[3,4]], r = 1, c = 4
            Output: [[1,2,3,4]]

            Input: mat = [[1,2],[3,4]], r = 2, c = 4
            Output: [[1,2],[3,4]]
            (illegal --> output the original matrix)
        """
        arr_1dim = [col for row in mat for col in row]
        if r * c != len(arr_1dim):
            return mat
        return [arr_1dim[i * c:(i + 1) * c] for i in range(r)]


if __name__ == "__main__":
    sol = Solution()
    arr = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(sol.matrixReshape(arr, r, c))


