from collections import Counter

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Given two integer arrays nums1 and nums2, return an array of their intersection.

        Args:
            nums1 (list[int]): The first integer array.
            nums2 (list[int]): The second integer array.

        Returns:
            list[int]: A new array containing the intersection of `nums1` and `nums2`.
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # Update count1 in-place with common elements in count2 and their minimum counts
        count1 &= count2

        # Extract keys (elements) from the updated Counter
        return list(count1.keys())


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 6, 7, 8]
    print(sol.intersection(nums1, nums2))