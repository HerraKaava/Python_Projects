class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """
        Given 0-indexed 1-dimensional integer array 'original', and two integers 'm' and 'n',
        creates a 2-dimensional array with m rows and n columns.

        Examples:
            Input: original = [1,2,3], m = 1, n = 3
            Output: [[1,2,3]]

            Input: original = [1,2,3,4], m = 2, n = 2
            Output: [[1,2],[3,4]]

            Input: original = [1,2], m = 1, n = 1
            Output: []
            (not possible --> empty array)
        """
        if n * m != len(original):
            return []    # Incorrect dimensions --> return an empty array
        return [original[i*n:(i+1)*n] for i in range(m)]


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6]
    m = 2
    n = 3
    x = sol.construct2DArray(arr, m, n)
    print(x)

