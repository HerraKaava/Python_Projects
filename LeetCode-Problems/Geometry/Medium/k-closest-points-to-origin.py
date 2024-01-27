import numpy as np

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Given an array of points where points[i] = [xi,yi] represents a point
        on the xy plane and an integer k, finds the k closest points to the origin (0,0).

        The distance between two points on the xy plane is calculated using the Euclidian distance.
        """
        if not points or not points[0]:
            return []

        # Sort the coordinates based on their distance to the origin
        return sorted(points, key=lambda x: np.sqrt((x[0] - 0)**2 + (x[1] - 0)**2))[:k]


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 3], [-2, 2]]
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k = 1
    k2 = 2
    print(sol.kClosest(points2, 2))
