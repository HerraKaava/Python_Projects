class Solution:
    def plusOne(self, digits):
        """
        Given a list of non-negative integers representing a non-negative integer,
        increment the integer by 1. The digits are stored in reverse order,
        and each element of the list contains a single digit.

        Args:
            digits (list[int]): A list of non-negative integers representing a non-negative integer.

        Returns:
            list[int]: A list containing the digits of the integer after incrementing by 1.

        Example:
            sol = Solution()
            sol.plusOne([1, 2, 3]) --> [1, 2, 4]
            sol.plusOne([9, 9]) --> [1, 0, 0]
        """
        s1 = ""    # A string used to temporarily convert the integers of the input list into a string
        for j in digits:
            s1 += str(j)
        s2 = int(s1)    # Convert the string temporarily back into type: 'int' to add 1 into it
        s2 += 1
        s3 = str(s2)    # Back into a string
        # Add the strings (as integers) back into an array.
        # To add the individual digits of the integer back into an array,
        # it is required that we are dealing with a string rather than an integer,
        # since 'int' object is not subscriptable.
        arr = []
        for i in range(len(s3)):
            arr.append(int(s3[i]))
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))    # [1, 2, 4]
    print(sol.plusOne([1, 2, 9]))    # [1, 3, 0]
    print(sol.plusOne([9, 9]))       # [1, 0, 0]
