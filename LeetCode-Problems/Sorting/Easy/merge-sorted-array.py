class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merge the arrays nums1 and nums2 into a single array sorted in ascending order.

        Args:
            nums1 (list): The first array to be merged.
            nums2 (list): The second array to be merged.
            m (int): The number of elements in nums1.
            n (int): The number of elements in nums2.

        Returns:
            None.

        The final sorted array should not be returned by the function,
        but instead be stored inside the array nums1. To accommodate this,
        nums1 has a length of m + n,
        where the first m elements denote the elements that should be merged,
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # Replace the zeros in the array nums1 with elements from the array nums2
        j = 0
        for i in range(m, m + n):
            nums1[i] = nums2[j]
            j += 1

        # Call the merge_sort() function with the nums1 array (merge_sort is implemented below)
        return self.merge_sort(nums1)

    # Use merge sort algorithm to sort the array in ascending order.
    # Merge sort algorithm has a time complexity of O(n * log(n)),
    # which is the optimal time complexity for comparison based algorithms
    def merge_sort(self, input_list: list[int]):
        """
        Sorts a given list (in-place) in ascending order using the merge sort algorithm.

        Args:
            input_list (list): The list to be sorted.

        Returns:
            list: The modified list containing the sorted elements from the input list.

        Notes:
            - The merge sort is a divide and conquer algorithm,
              which essentially means that the problem is recursively broken down into multiple subproblems
              until they become simple to solve.
              The solutions of the subproblems are then combined to solve the original problem.

            - The merge sort algorithm has a time complexity of O(n * log(n)),
              which is the optimal time complexity for comparison based algorithms.

        General principle of the merge sort algorithm:
            1. Split array in half
            2. Call merge sort on each half to sort them recursively
            3. Merge both sorted halves into one sorted array.
        """
        # If the length of the array is <= 1, there is nothing to sort.
        if len(input_list) <= 1:
            return input_list

        else:
            left_arr = input_list[:len(input_list)//2]    # From the beginning to the middle of the array
            right_arr = input_list[len(input_list)//2:]   # From the middle to the end of the array

            # Recursively call the merge_sort() function
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            # In the merge step, the left-most element of an array is compared
            # to the left-most element of another array.
            i = 0    # The index of the left-most element of the left array
            j = 0    # The index of the left-most element of the right array
            k = 0    # The index of the merged array

            while i < len(left_arr) and j < len(right_arr):
                # If the left-most element of the left array is smaller than the left-most element of the right array,
                # it goes first into the merged array.
                if left_arr[i] < right_arr[j]:
                    input_list[k] = left_arr[i]
                    i += 1
                else:
                    # Otherwise the left-most element of the right array goes first into the merged array.
                    input_list[k] = right_arr[j]
                    j += 1
                k += 1

            # Assign the remaining elements from the left array into the merged array
            while i < len(left_arr):
                input_list[k] = left_arr[i]
                i += 1
                k += 1

            # Assign the remaining elements from the right array into the merged array
            while j < len(right_arr):
                input_list[k] = right_arr[j]
                j += 1
                k += 1

            return input_list


if __name__ == "__main__":
    sol = Solution()
    l1 = [4, 5, 6, 7, 0, 0, 0]
    l2 = [1, 2, 3]
    print(sol.merge(l1, 4, l2, 3))      # [1, 2, 3, 4, 5, 6, 7]
    print(sol.merge([1], 1, [0], 0))    # [1]
    print(sol.merge([0], 0, [1], 1))    # [1]

