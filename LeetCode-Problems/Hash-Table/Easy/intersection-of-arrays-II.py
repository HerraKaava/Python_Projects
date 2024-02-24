from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Given two integer arrays nums1 and nums2, return the array of their intersection.
        Each element will appear as many times as it appears in both arrays.

        Examples:
            Input: nums1 = [1,2,2,1], nums2 = [2,2]
            Output: [2,2]

            Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
            Output: [4,9]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # Update count1 to only include the intersection of count1 and count2
        count1 &= count2

        result = []
        for key, val in count1.items():
            result.extend([key] * val)

        return result


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1, 1, 1, 1]
    nums2 = [2, 2, 1, 1, 1, 1]
    print(sol.intersect(nums1, nums2))
