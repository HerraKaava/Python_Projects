class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        """
        Given an array of points on the xy-plane, where points[i] = [xi,yi],
        Finds the minimum area of a rectangle formed by these points,
        with sides parallel to the x and y axes.

        Example:
            Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
            Output: 4
        """
        # In this task, 4 points are needed to form a rectangle.
        if len(points) < 4:
            return 0

        # For any two points to be opposite corners (diagonals) of a rectangle,
        # they must have different x and y coordinates.
        # If one identifies a pair of points that could be the opposite corners of a rectangle,
        # one then needs to check if the other two corners of that rectangle exist.

        # Consider the following example.
        # If you have the points (1,2) and (3,4),
        # the other two corners of that rectangle would be (1,4) and (3,2).
        # This is because if you draw these points on a plane,
        # you'll notice that the two missing corners can be formed by
        # swapping the x-coordinates between those two points
        # (i.e., pairing the x-coordinate with the opposite corners y-coordinate).

        p_set = set(tuple(p) for p in points)    # list[list] -> set(tuple) for faster search
        min_rectangle_area = float('inf')
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in p_set and (p2[0], p1[1]) in p_set:

                        P1 = [p1[0], p1[1]]
                        P2 = [p2[0], p2[1]]
                        P3 = [p1[0], p2[1]]    # We only need the third corner to calculate the area

                        # Since both of these points P3 and P1 share the same x-coordinate,
                        # the distance (height) is just the absolute value of the difference
                        # of their y-coordinates
                        height = abs(P3[1] - P1[1])

                        # Since both of these points P3 and P2 share the same y-coordinate,
                        # the distance (width) is just the absolute value of the difference
                        # of their x-coordinates
                        width = abs(P3[0] - P2[0])

                        rectangle_area = height * width
                        min_rectangle_area = min(min_rectangle_area, rectangle_area)

        return int(min_rectangle_area) if min_rectangle_area != float('inf') else 0


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    print(sol.minAreaRect(points))






