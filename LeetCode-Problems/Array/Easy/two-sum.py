class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find indices of two numbers in the array 'nums' that add up to the given 'target'.

        Notes:
            It is assumed that each input has exactly one solution,
            and the same element should not be used twice.
        """
        # This problem can be tackled e.g. using a nested loop.
        for i in range(len(nums) - 1):
                for j in range(i+1, len(nums)):
                    if (nums[i] + nums[j] == target) and (i != j):
                        return [i, j]

        # Every element of the array is compared to every other element in the array.
        # e.g., in the first iteration, nums[0] is compared to nums[1], nums[2], ... , nums[n].
        # If a "match" is found (i.e. two numbers add up to the value of 'target'),
        # the indices of those numbers are returned.
        # The condition "i != j" ensures that the same element of the array won't be used twice.
        # It is worth noting that this algorithm has a time complexity of O(n^2),
        # which is not optimal for comparison based algorithms.


if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 2, 4]
    nums3 = [3, 2, 3]
    nums4 = [2,5,5,11]
    print(sol.twoSum(nums1, 9))    # [0, 1]
    print(sol.twoSum(nums2, 6))    # [1, 2]
    print(sol.twoSum(nums3, 6))    # [0, 2]
    print(sol.twoSum(nums4, 10))   # [1, 2]
