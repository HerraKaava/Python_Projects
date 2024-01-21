class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        """
        Given 0-indexed 2D integer array 'nums',
        performs the following operations until the matrix becomes empty:

        1. From each row in the matrix, select the largest number and remove it.
           In the case of a tie, it does not matter which number is chosen.

        2. Identify the highest number amongst all those removed in step 1.
           Add that number to your score.

        Example:
            Input: nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
            Output: 15
            Explanation: In the first operation, we remove 7, 6, 6, and 3.
            We then add 7 to our score. Next, we remove 2, 4, 5, and 2.
            We add 5 to our score. Lastly, we remove 1, 2, 3, and 1.
            We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.
        """
        score = 0
        for i in range(len(nums[0])):
            score += max([row.pop(row.index(max(row))) for row in nums])
        return score


if __name__ == "__main__":
    sol = Solution()
    nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
    print(sol.matrixSum(nums))