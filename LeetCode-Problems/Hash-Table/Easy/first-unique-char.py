class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Given string s, finds the first non-repeating character in s
        and returns its index. If it does not exist, returns -1 instead.

        Notes:
            - s consists of only lowercase English letters.

        Examples:
            Input: s = "leetcode"
            Output: 0

            Input: s = "aabb"
            Output: -1
        """
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        unique_chars = [key for (key, val) in char_count.items() if val == 1]
        return s.index(unique_chars[0]) if unique_chars else -1


if __name__ == "__main__":
    sol = Solution()
    s = "aabb"
    print(sol.firstUniqChar(s))