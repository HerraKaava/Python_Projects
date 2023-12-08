class Solution:
    def pascal_triangle(self, numRows: int) -> list[list[int]]:
        # A list to store the rows of Pascal's triangle
        l1 = []
        # A helper variable for the inner loop
        j = 1
        for _ in range(numRows):
            # This list is used to generate the rows of Pascal's triangle
            l2 = []
            # The first row of Pascal's triangle has 1 element, second has 2 elements etc.
            # This is why j starts from 1 and gets increased after each iteration round.
            for i in range(j):
                # Every row of Pascal's triangle has the number 1 as the first and last element.
                # If i == 0, it means that a new row is starting and 1 should be added to that row.
                if i == 0:
                    l2.append(1)
                # If i == j-1, it means that we have reached the end of the row, and 1 should be added.
                elif i == j-1:
                    l2.append(1)
                else:
                    # j starts from 1 and Python indexing starts from 0.
                    # So to get the previous "row" (list) of the nested list l1,
                    # we need to index j-2.
                    # e.g., if j = 3, then to get row 2 of the nested list, we need j-2 = 1.
                    l2.append(l1[j-2][i] + l1[j-2][i-1])
            l1.append(l2)
            j += 1
        return l1


    # Uncommented version
    def pascal_triangle2(self, numRows: int) -> list[list[int]]:
        l1 = []
        j = 1
        for _ in range(numRows):
            l2 = []
            for i in range(j):
                if i == 0:
                    l2.append(1)
                elif i == j-1:
                    l2.append(1)
                else:
                    l2.append(l1[j-2][i] + l1[j-2][i-1])
            l1.append(l2)
            j += 1
        return l1


if __name__ == "__main__":
    sol = Solution()
    print(sol.pascal_triangle(5))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]