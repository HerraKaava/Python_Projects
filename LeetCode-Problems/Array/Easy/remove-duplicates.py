class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Given an integer array nums sorted in ascending order,
        remove the duplicates in-place such that each unique element appears only once in the array.
        The relative order of the elements are kept the same.

        Args:
            nums (list[int]): The list to be sorted.

        Returns:
            k (int): The number of unique elements in nums.
        """
        i = 0
        # Outer loop iterates until all elements have been compared
        while i < len(nums):
            j = i + 1
            # Inner loop compares the i-th element with subsequent elements to find duplicates
            while j < len(nums):
                if nums[i] == nums[j]:
                    # If a duplicate is found, remove the j-th element
                    nums.pop(j)
                else:
                    # If no duplicate, move to the next element
                    j += 1
            # Move to the next element for comparison
            i += 1
        return len(nums)

        # Line 14: a helper variable i=0 is created to keep track of the ith element
        # that is being compared to i+1th element.
        # Line 15: a condition i<len(nums) is set.
        # When this condition becomes False, the duplicates have been successfully removed.
        # Line 16: a helper variable is created to keep track of the i+1th element.
        # Line 17: this condition ensures that i+1,i+2,...,n are compared to the ith element of the array.
        # This is true because on line 18, if the ith and jth element are equal to each other,
        # the latter (jth element) gets popped (removed) from the array.
        # From this it follows that the index of every element
        # to the right of the removed element (jth) gets decreased by 1.
        # In this case, we don't need to increase the value of j to compare the ith element
        # of the array to the i+1th element of the array (because of the reason stated on lines 32-33).
        # On the other hand, if a duplicate is not found,
        # we increase the value of j on line 21 to again compare the ith element to i+1th element.
        # After the inner while loop is done (while j < len(nums) --> False),
        # we increase the value of i by 1.
        # This is because on the 1st iteration,
        # the first element of the array is compared to every other element in the array.
        # After this, we need to increase the value of i by 1 so that the second element of the array
        # gets compared to every other element in the array etc...


if __name__ == "__main__":
    sol = Solution()
    l1 = [4, 4, 2, 5, 2, 1, 3, 1, 1, 1, 2]
    l2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print(sol.removeDuplicates(l1))      # 5
    print(l1)                            # [4, 2, 5, 1, 3]
    print(sol.removeDuplicates(l2))      # 1
    print(l2)                            # [5]