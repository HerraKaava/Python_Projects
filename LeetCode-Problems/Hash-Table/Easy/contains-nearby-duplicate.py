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
        d = {}
        for idx, num in enumerate(nums):
            if num in d and abs(idx - d[num]) <= k:
                # Duplicate found in the desired range
                return True
            # Update the index of the current key
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
