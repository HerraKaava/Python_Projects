class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        """
        Finds the distance from the cell (rCenter, cCenter) to all other cells.
        The coordinates of the cells will be sorted by their distance to (rCenter, cCenter)
        from the smallest distance to the largest distance.

        Notes:
            - The distance between the points will be calculated using the Manhattan distance,
             which is calculated as the sum of the absolute differences between the two vectors.

        Examples:
            Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
            Output: [[0,0],[0,1]]
            Explanation: The distances from (0, 0) to other cells are: [0,1]
            Note that the distance from the cell (rCenter, cCenter) to itself
            will always be zero.

            Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
            Output: [[0,1],[0,0],[1,1],[1,0]]
            Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
            The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
        """
        coordinates = []
        for i in range(rows):
            for j in range(cols):
                coordinates.append([i, j])
        return sorted(coordinates, key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))


    def all_cells_dist_order(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        """
        A more efficient version of the function
        """
        return sorted([[r, c] for r in range(rows) for c in range(cols)], \
                      key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))


if __name__ == "__main__":
    sol = Solution()
    rows = 2
    cols = 2
    rCenter = 0
    cCenter = 1
    print(sol.allCellsDistOrder(rows, cols, rCenter, cCenter))
