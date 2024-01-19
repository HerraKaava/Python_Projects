class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Given a grid of size m x n and an integer k, Shift the grid k times.

        grid[i][j]  -->  grid[i][j+1]
        grid[i][n-1]  -->  grid[i+1][0]
        grid[m-1][n-1]  -->  grid[0][0]
        """
        def matrix_to_1D(grid):
            """
            Flattens a 2D grid to 1D.

            Notes:
                This can be done using NumPys flatten() method (on a NumPy array),
                but this function will use a list comprehension.
            """
            return [col for row in grid for col in row]

        def shift_k_times(grid_1D, k):
            """
            Notes:
                - Shifting a list of 5 elements 10 times is the same as shifting it 0 times.
                - If n=5 and k=7 e.g., then k % n = 2
                --> Shifting a list of 5 elements 7 times is the same as shifting it 2 times.
            """
            n = len(grid_1D)
            k = k % n
            for i in range(k):
                grid_1D = grid_1D[-1:] + grid_1D[:-1]
            return grid_1D

        def oneDim_to_twoDim(grid_1D):
            """
            Converts 1D array into a 2D array.
            """
            m = len(grid)
            n = len(grid[0])
            return [grid_1D[i*n:(i+1)*n] for i in range(m)]

        grid_1D = matrix_to_1D(grid)
        shifted_grid_1D = shift_k_times(grid_1D, k)
        return oneDim_to_twoDim(shifted_grid_1D)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    grid2 = [[1],[2],[3],[4],[7],[6],[5]]
    k = 3
    k2 = 23
    print(sol.shiftGrid(grid, k))
    print(sol.shiftGrid(grid2, k2))

