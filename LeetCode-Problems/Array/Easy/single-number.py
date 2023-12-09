class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the unique element in a non-empty array of integers,
        where each element appears twice except for one.
        The unique element will be searched using a linear runtime complexity and constant extra space.

        Args:
            nums (list[int]): A non-empty list of integers.

        Returns:
            int: The unique element that appears only once in the array.

        Example:
        s = Solution()
        s.singleNumber([2, 2, 1, 3, 3]) --> 1
        """
        # To achieve a linear runtime complexity and constant space complexity,
        # one can use bitwise XOR operation.
        # The idea is based on the property that XOR of two same numbers is 0,
        # and XOR of a number with 0 is the number itself.
        # By XORing all elements in the list, the duplicates cancel each other out,
        # leaving only the unique element.
        lonely_num = 0
        for i in nums:
            lonely_num ^= i
        return lonely_num


if __name__ == "__main__":
    sol = Solution()
    l1 = [1, 0, 1, 0, 2, 2, 5, 4, 5]
    l2 = [1, 0, 1]
    l3 = [1]
    print(sol.singleNumber(l1))    # 4
    print(sol.singleNumber(l2))    # 0
    print(sol.singleNumber(l3))    # 1






