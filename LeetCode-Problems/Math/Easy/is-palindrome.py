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
        return str(x) == str(x)[::-1]
                

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1001))    # True
    print(sol.isPalindrome(1002))    # False

