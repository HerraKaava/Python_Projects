class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k,
        Find if there are two distinct indices i and j in the array nums such that
        nums[i] == nums[j] and abs(i-j) <= k

        Args:
            nums (list[int]): The integer array to be checked.
            k (int): The integer that works as a threshold for which abs(i-j) <=k has to be true.

        Returns:
            bool: True if there are two distinct indices i and j such that
            nums[i] == nums[j] and abs(i-j) <= k, False otherwise.

        Examples:
            Input: nums = [1,2,3,1], k = 3
            Output: true

            Input: nums = [1,0,1,1], k = 1
            Output: true

            Input: nums = [1,2,3,1,2,3], k = 2
            Output: false
        """
        # Initialize a dictionary to store the key-value pairs (element: index of the element)
        d = {}
        for idx, num in enumerate(nums):
            # If the element (num) is already in the dictionary,
            # check if the difference between the current index (idx)
            # and the index of the duplicate value (d[num])
            # is less than or equal to the threshold (k).
            if num in d.keys() and abs(idx - d[num]) <= k:
                # If the condition is met, return True.
                return True
            else:
                # If the element is not present in the dictionary,
                # set the element as the key and the index of the element as the value.
                d[num] = idx
        return False


    # Uncommented version
    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d.keys() and abs(idx - d[num]) <= k:
                return True
            else:
                d[num] = idx
        return False


    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        """
        A solution that uses a slightly different approach to solve the problem.
        Note that this approach is less efficient.
        """
        d = {}
        for idx, key in enumerate(nums):
            if key not in d:
                d[key] = [idx]
            else:
                d[key].append(idx)

        for key, val in d.items():
            if len(val) > 1:
                for i in range(len(val)-1):
                    for j in range(i+1, len(val)):
                        if abs(val[i] - val[j]) <= k:
                            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 0, 1, 1]
    nums3 = [1, 2, 3, 1, 2, 3]
    print(sol.containsNearbyDuplicate(nums1, 3))    # True
    print(sol.containsNearbyDuplicate(nums2, 1))    # True
    print(sol.containsNearbyDuplicate(nums3, 2))    # False
