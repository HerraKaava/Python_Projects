class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s which consists of lowercase or uppercase letters,
        finds the length of the longest palindrome that can be built with those letters.

        Notes:
            - Letters are case sensitive (e.g., "Aa" is not considered a palindrome).

        Examples:
            Input: s = "abccccdd"
            Output: 7
            Explanation: One longest palindrome that can be built is "dccaccd",
            whose length is 7.
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # Create a dictionary containing the character counts of the string.
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        longest_palindrome = 0
        odd = False
        for count in char_count.values():
            if count % 2 == 0:
                # Even counts can directly be added to the length of the longest palindrome
                longest_palindrome += count
            else:
                # The even part of an odd count can be added to the length of the longest palindrome
                longest_palindrome += count - 1
                odd = True

        # One char from any of the odd counts can be added to the middle of the palindrome
        if odd:
            longest_palindrome += 1

        return longest_palindrome


if __name__ == "__main__":
    sol = Solution()
    s = "abccccdd"
    s2 = "bananas"
    s3 = "bb"
    print(sol.longestPalindrome(s))
    print(sol.longestPalindrome(s2))
    print(sol.longestPalindrome(s3))