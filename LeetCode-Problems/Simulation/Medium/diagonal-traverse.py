class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Given an m x n matrix 'mat',
        return an array containing all the elements of 'mat',
        arranged in diagonal order.

        Example:
            Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [1,2,4,7,5,3,6,8,9]
        """
        m = len(mat)
        n = len(mat[0])
        # If the matrix has no elements, return an empty array.
        if (not m) or (not n):
            return []

        # The logic behind the solution:

            # For an m x n matrix, there is m + n - 1 diagonals.
            # When looking at the indices of the elements of the matrix,
            # an observation can be made:
            # The sum of the index of the a_{ij}th element will correspond to the diagonal
            # that it belongs to on a 0-indexed ordered scale 0,1,2,...,m+n-1.

            # For example, if A = [[1,2,3],[4,5,6],[7,8,9]], it is clear that
            # A is an 3x3 matrix --> A will have 3+3-1=5 diagonals.
            # 7 has an index of (2,0), 5 has an index of (1,1) and 3 has an index of (0,2).
            # Notice that 2+0=2, 1+1=2, 0+2=2 --> these elements belong to the third diagonal.

        def add_diagonals(mat: list[list[int]]) -> list[list[int]]:
            """
            Adds the m+n-1 diagonals to a matrix.
            Note that after this some of the elements are still in wrong order.
            """
            arr = [[] for i in range(m+n-1)]
            for i in range(m):
                for j in range(n):
                    sum_indices = i+j
                    arr[sum_indices].append(mat[i][j])
            return arr

        def flip_diagonals() -> list[list[int]]:
            """
            Flips every other diagonal.
            This way the elements will be in the correct order.
            """
            arr = add_diagonals(mat)
            k = 0
            for row in arr:
                if k % 2 == 0:
                    row[:] = row[::-1]
                k += 1
            return arr

        def twoD_to_oneD():
            arr = flip_diagonals()
            return [col for row in arr for col in row]

        return twoD_to_oneD()


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.findDiagonalOrder(mat))




