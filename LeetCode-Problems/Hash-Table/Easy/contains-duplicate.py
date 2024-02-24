from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, find if the array contains duplicate values
        (i.e., find if any value appears at least twice in the array).

        Args:
            list[int]: The list to be checked for duplicate values.

        Returns:
            bool: True if the array contains duplicate values, False otherwise.
        """
        # Use Counter from collections to count the occurrences of each number in nums
        num_counts = Counter(nums)
        return any(i > 1 for i in num_counts.values())
        # any() is a built-in function that returns True if at least one element of an iterable is true.
        # If the iterable is empty, it returns False.


    def contains_duplicate(self, nums: list[int]) -> bool:
        """
        Another version. 
        Without Counter and using all() instead of any().
        """
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        return not all(val == 1 for (key, val) in num_count.items())
        

if __name__ == "__main__":
    sol = Solution()
    l1 = [1, 2, 3, 4]
    l2 = [1, 1, 2, 3]
    print(sol.containsDuplicate(l1))    # False
    print(sol.containsDuplicate(l2))    # True

