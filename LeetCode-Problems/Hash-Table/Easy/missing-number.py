class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array.

        Examples:
            Input: nums = [3,0,1]
            Output: 2

            Input: nums = [0,1]
            Output: 2

            Input: nums = [9,6,4,2,3,5,7,0,1]
            Output: 8

        Notes:
            All the numbers of nums are unique.
        """
        # The sum of n natural numbers 0,1,2,...,n can be calculated using the classic formula:
        # S_n = n*(n+1)/2
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        observed_sum = sum(nums)
        return expected_sum - observed_sum


    def missing_num(self, nums: list[int]) -> int:
        """
        A more efficient function.
        """
        nums_set = {num for num in range(1, len(nums)+1)}
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
        return next(iter(nums_set)) if nums_set else 0


if __name__ == "__main__":
    sol = Solution()
    nums1 = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9,6,4,2,3,5,7,0,1]
    print(sol.missingNumber(nums1))
    print(sol.missingNumber(nums2))
    print(sol.missingNumber(nums3))
