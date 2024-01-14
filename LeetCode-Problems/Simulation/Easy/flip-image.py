class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Given an n x n binary matrix image, flips the image horizontally and inverts it.

        Notes:
            - To flip an image horizontally means that each row of the image is reversed.
            - To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
        """
        return [[1 - i for i in row[::-1]] for row in image]


if __name__ == "__main__":
    sol = Solution()
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(sol.flipAndInvertImage(image))
