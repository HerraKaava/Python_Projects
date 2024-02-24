class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> set[int]:
        """
        Given two integer arrays nums1 and nums2, find their intersection.
        """
        return set(nums1) & set(nums2)


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 6, 7, 8]
    print(sol.intersection(nums1, nums2))
