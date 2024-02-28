class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        """
        Given an array of points on the xy-plane, where points[i] = [xi,yi],
        Finds the minimum area of a rectangle formed by these points,
        with sides parallel to the x and y axes.

        Example:
            Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
            Output: 4

        About the implementation of the function:

            For any two points to be opposite corners (diagonals) of a rectangle,
            they must have different x and y coordinates.

            If one identifies a pair of points that could be the opposite corners of a rectangle,
            one then needs to check if the other two corners of that rectangle exist.

            Consider the following example.
            If you have the points (1,2) and (3,4),
            the other two corners of that rectangle would be (1,4) and (3,2).
            This is because if you draw these points on a plane,
            you'll notice that the two missing corners can be formed by
            swapping the x-coordinates between those two points
            (i.e., pairing the x-coordinate with the opposite corners y-coordinate).
        """
        if len(points) < 4:
            return 0
        p_set = set(tuple(p) for p in points)   # list[list] -> set(tuple) for faster search
        min_area = float('inf')
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    p3 = (p1[0], p2[1])
                    p4 = (p2[0], p1[1])
                    if p3 in p_set and p4 in p_set:
                        area = abs(p3[1] - p1[1]) * abs(p3[0] - p2[0])
                        if area < min_area:
                            min_area = area
        return min_area if min_area != float('inf') else 0


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    print(sol.minAreaRect(points))





