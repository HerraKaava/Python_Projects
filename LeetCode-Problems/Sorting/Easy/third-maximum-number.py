class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        """
        Finds the third distinct maximum number in the array 'nums'.
        If the third maximum does not exist, finds the largest.

        Examples:
            Input: nums = [3,2,1]
            Output: 1

            Input: nums = [1,2]
            Output: 2
        """
        nums = sorted(list(set(nums)))    # Sort and remove the duplicates
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]


if __name__ == "__main__":
    sol = Solution()
    nums1 = [3, 2, 1]
    nums2 = [1, 2]
    nums3 = [2, 2, 3, 1]
    print(sol.thirdMax(nums1))
    print(sol.thirdMax(nums2))
    print(sol.thirdMax(nums3))


