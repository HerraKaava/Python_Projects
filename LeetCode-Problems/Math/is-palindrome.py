class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if the given integer x is a palindrome.
        A palindrome is a number that reads the same backward as forward.

        Args:
            x (int): The integer to be checked.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        s1 = str(x)
        s2 = ""
        # Construct the string backwards in the loop.
        # If x = 123, then s1 = "123" and s2 = "321".
        for i in range(len(s1)-1, -1, -1):
            s2 += s1[i]
        if s1 == s2:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1001))    # True
    print(sol.isPalindrome(1002))    # False

