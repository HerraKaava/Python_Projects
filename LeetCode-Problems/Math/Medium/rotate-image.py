class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Given a 2D matrix representing an image,
        rotates the image by 90 degrees (clockwise) in-place.

        Examples:
            Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [[7,4,1],[8,5,2],[9,6,3]]

            Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
            Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        """
        matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
        # zip(*matrix) effectively transposes the rows of the matrix,
        # and row[::-1] reverses the order of each row.

        # m = [[1,2,3],[4,5,6],[7,8,9]].
        # r1 = [1, 2, 3]
        # r2 = [4, 5, 6]
        # r3 = [7, 8, 9]

        # zip(*m) and zip(r1, r2, r3) are equivalent.

        # When you use the * operator with zip(*m), 
        # it unpacks the nested list m into separate arguments, 
        # effectively passing each inner list as a separate argument to zip. 
        # So zip(*m) is equivalent to zip([1, 2, 3], [4, 5, 6], [7, 8, 9]).


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    print(matrix)
