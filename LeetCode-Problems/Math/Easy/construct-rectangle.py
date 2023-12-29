class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        """
        Given a rectangular web page’s area,
        finds the optimal measurements (length, width) of the web page,
        while satisfying the following conditions:

        1. The area of the rectangular web page must equal to the given target area.
        2.The width W should not be larger than the length L, which means L >= W.
        3.The difference between length L and width W should be as small as possible.

        Args:
            area (int): The area of the rectangular web page.

        Returns:
            list[int]: A list containing the length and width of the rectangular web page.
        """
        # Find all the factors of 'area'
        factors = []
        for num in range(1, area+1):
            if area % num == 0:
                factors.append(num)

        # Construct all the possible factor pairings (L, W),
        # and choose the most optimal in terms of the conditions.
        factor_pairs = [(x, y) for x in factors for y in factors if x >= y and x * y == area]
        optimal_pair = min(factor_pairs, key=lambda x: x[0] - x[1])
        return list(optimal_pair)


if __name__ == "__main__":
    sol = Solution()
    print(sol.constructRectangle(50))        # [10, 5]
    print(sol.constructRectangle(122122))    # [427, 286]


