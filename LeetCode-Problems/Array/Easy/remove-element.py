class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Removes all occurrences of the specified value 'val' in the given integer array 'nums' in-place.

        Args:
            nums (list[int]): The input integer array.
            val (int): The value to be removed from 'nums'.

        Returns:
            int: The number of elements in 'nums' after removal of 'val'.

        Notes:
            The order of the remaining elements may be changed.
        """
        # A helper variable for the while loop
        i = 0
        # Iterate until we reach the end of the array
        while i < len(nums):
            if nums[i] == val:
                # When encountering the specified value 'val', remove it.
                # Note that after popping an element from a Python list,
                # all the elements to the right of the removed element get shifted to the left
                # (i.e., all the elements j,j+1,...,n in the array move one index position to the left).
                # This means that after popping an element from the list,
                # one does not need to increase the index i to compare the current element to the next element.
                nums.pop(i)
            else:
                # Increase the index i only when nums[i] != val
                i += 1
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    l1 = [3,2,2,3]
    l2 = [5, 5, 5, 5, 5, 5, 5, 0]
    print(sol.removeElement(l1, 2))    # 2
    print(l1)                          # [3, 3]
    print(sol.removeElement(l2, 5))    # 1
    print(l2)                          # [0]