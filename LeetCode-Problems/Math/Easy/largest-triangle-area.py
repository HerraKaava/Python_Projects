from itertools import combinations
import numpy as np


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Given an array of points on the xy plane,
        finds the largest triangle that can be formed by any three different points

        Examples:
            Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
            Output: 2.00000

            Input: points = [[1,0],[0,0],[0,1]]
            Output: 0.50000

        Notes:
            - All the given points are unique.
        """
        # Given three points, one can calculate the area of triangle using a determinant.
        # Construct a nested list that contains matrices in the following form:

        #               |x1  y1  1|
        #               |x2  y2  1|
        #               |x3  y3  1|, where (x1,y1), (x2,y2), (x3,y3) are the three points forming the triangle.

        # Note that a column of ones has to be added since determinants are defined only for square matrices.
        # These matrices will be used to calculate the determinants.
        # The area of the respective triangle is the determinant multiplied by 0.5

        three_point_tuples = list(combinations(points, 3))
        array_list = []
        for p1, p2, p3 in three_point_tuples:
            arr = np.array([[p1[0], p2[0], p3[0]],
                            [p1[1], p2[1], p3[1]],
                            [1, 1, 1]])
            array_list.append(arr.T)

        triangle_area_array = []
        for array in array_list:
            triangle_area = np.linalg.det(array) * (1 / 2)
            # The area of a triangle cannot be negative, but determinant, however, can be negative.
            # --> if the result is negative, reverse the sign.
            if triangle_area < 0:
                triangle_area *= -1
            triangle_area_array.append(triangle_area)

        return max(triangle_area_array)


if __name__ == "__main__":
    sol = Solution()
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(sol.largestTriangleArea(points))


