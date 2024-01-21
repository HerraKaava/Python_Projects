class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        """
        Given an m x n matrix grid consisting of positive integers,
        performs the following operation until grid becomes empty:

        Delete the element with the greatest value from each row.
        If multiple such elements exist, delete any of them.
        Add the maximum of deleted elements to the answer.
        """
        result = 0
        for i in range(len(grid[0])):
            result += max([row.pop(row.index(max(row))) for row in grid])
        return result


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2, 4], [3, 3, 1]]
    print(sol.deleteGreatestValue(grid))
