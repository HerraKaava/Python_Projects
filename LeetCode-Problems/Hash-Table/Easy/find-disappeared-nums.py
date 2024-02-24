class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> set[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n],
        finds all the integers in the range [1, n] that do not appear in nums.

        Examples:
            Input: nums = [4,3,2,7,8,2,3,1]
            Output: [5,6]

            Input: nums = [1,1]
            Output: [2]

        Notes:
            This function has a time complexity of O(n).

            The reasons for this are:

            Membership test ('in'): checking if an item is in a set
            is significantly faster than checking if an item is in a list.
            The time complexity is O(1) in the average case,
            thanks to the underlying hash table structure of sets.
            This allows for a very fast determination of whether an item
            is present in the set.

            Remove operation: removing an item from a set also benefits
            from the hash table structure, with a time complexity of O(1)
            in the average case, because it directly accesses the item
            without needing to shift elements around (unlike a list).

            Therefore, this function operates with a time complexity of O(n),
            because each operation (checking or membership and removing an item)
            can be done in a constant time, and these operations are performed
            once for each of the n elements in nums.

            See the time complexities in:
            https://wiki.python.org/moin/TimeComplexity
        """
        missing_nums = {num for num in range(1, len(nums)+1)}
        for val in nums:
            if val in missing_nums:
                missing_nums.remove(val)
        return missing_nums


    def find_disappeared_nums(self, nums: list[int]) -> list[int]:
        """
        This function function provides the exact same functionality
        as the findDisappearedNumbers(), but this one uses
        a list to store the range of the values 1,2,...,n.
        This leads to a time complexity of O(n^2).

        This is because...

            - Checking if an item is in a list has
              an average case time complexity of O(n).

            - Removing an item from a list also has an average case
              time complexity of O(n). This is because after finding
              the element, the list has to be restructured to fill the gap
              left by the removed element, which involves shifting all
              the subsequent elements.
        """
        missing_nums = [num for num in range(1, len(nums) + 1)]
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
    print(sol.find_disappeared_nums(nums3))
