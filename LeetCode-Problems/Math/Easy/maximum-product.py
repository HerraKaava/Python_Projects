class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """
        Given an integer array nums, finds the maximum product of three numbers.

        Examples:
            Input: nums = [1,2,3]
            Output: 6

            Input: nums = [1,2,3,4]
            Output: 24

            Input: nums = [-1,-2,-3]
            Output: -6
        """
        if len(nums) < 3:
            raise ValueError('Length of the integer array must be atleast 3.')

        # The largest product is achieved by either...
        #   1. The product of the three largest numbers.
        #   2. The product of the two smallest numbers and the largest number.

        nums.sort()
        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]
        return max(product1, product2)


if __name__ == "__main__":
    sol = Solution()
    nums = [-5, -3, -2, 2]
    print(sol.maximumProduct(nums))
