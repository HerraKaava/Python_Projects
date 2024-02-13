class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n],
        finds all the integers in the range [1, n] that do not appear in nums.

        Examples:
            Input: nums = [4,3,2,7,8,2,3,1]
            Output: [5,6]

            Input: nums = [1,1]
            Output: [2]

        Notes:
            - n == nums.length
            - 1 <= n <= 10^5
            - 1 <= nums[i] <= n
        """
        missing_nums = {num for num in range(1, len(nums)+1)}
        for val in nums:
            if val in missing_nums:
                missing_nums.remove(val)
        return missing_nums


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    nums2 = [2, 2]
    nums3 = [1, 1, 1, 1]
    print(sol.findDisappearedNumbers(nums))
    print(sol.findDisappearedNumbers(nums2))
    print(sol.findDisappearedNumbers(nums3))
