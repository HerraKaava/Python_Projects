class MultiSortingAlgorithm:
    pass

    @staticmethod
    def bubble_sort(input_list):
        """
        Sorts a given list in ascending order using the bubble sort algorithm.
        This function does not modify the original list and returns a new sorted list.

        Args:
            input_list (list): The list to be sorted.

        Returns:
            list: A new list containing the sorted elements from the original input list.

        Notes:
            - The bubble sort is a brute force algorithm.
            - The bubble sort algorithm has a time complexity of O(n^2).
            - Static methods do not use the self parameter.
        """
        # Copy the original input list
        l_copy = input_list[:]
        for _ in range(len(l_copy)-1):
            for i in range(len(l_copy)-1):
                if l_copy[i+1] < l_copy[i]:
                    l_copy[i], l_copy[i+1] = l_copy[i+1], l_copy[i]
        return l_copy

    @staticmethod
    def insertion_sort(input_list):
        """
        Sorts a given list in ascending order using the insertion sort algorithm.
        This function does not modify the original list and returns a new sorted list.

        Args:
            input_list (list): The list to be sorted.

        Returns:
            list: A new list containing the sorted elements from the original input list.

        Notes:
            - The insertion sort is a brute force algorithm.
            - The insertion sort algorithm has a time complexity of O(n^2).
            - Static methods do not use the self parameter.
        """
        l_copy = input_list[:]
        for i in range(1, len(l_copy)):
            j = i
            while l_copy[j-1] > l_copy[j] and j > 0:
                l_copy[j-1], l_copy[j] = l_copy[j], l_copy[j-1]
                j -= 1
        return l_copy

    @staticmethod
    def selection_sort(input_list):
        """
        Sorts a given list in ascending order using the selection sort algorithm.
        This function does not modify the original list and returns a new sorted list.

        Args:
            input_list (list): The list to be sorted.

        Returns:
            list: A new list containing the sorted elements from the original input list.

        Notes:
            - The selection sort is a brute force algorithm.
            - The selection sort algorithm has a time complexity of O(n^2).
            - Static methods do not use the self parameter.
        """
        arr = input_list[:]
        for i in range(len(arr)-1):
            smallest_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[smallest_idx]:
                    smallest_idx = j
            arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]
        return arr

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
        # If the length of the array is less than 1, there is nothing to sort (and the recursion will stop).
        if len(input_list) > 1:
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
    sorting_alg = MultiSortingAlgorithm()
    l1 = [5, 2, 9, 10, 8, 7, 6, 1, 3, 4]
    l2 = [-5, 5, 4, 1, 3, -3, -2, 0, -1, 2, -4]
    l3 = [3, 5, 0, 2, 1, 4]
    l4 = [-3, 0, -5, -2, -1, -4]
    print(sorting_alg.bubble_sort(l1))
    print(sorting_alg.insertion_sort(l2))
    print(sorting_alg.selection_sort(l3))
    print(sorting_alg.merge_sort(l4))

