class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.
        Here "follow" means a full match, such that there is a bijection
        between a letter in pattern and a non-empty word in s.

        Examples:
            Input: pattern = "abba", s = "dog cat cat dog"
            Output: true

            Input: pattern = "abba", s = "dog cat cat fish"
            Output: false

            Input: pattern = "aaaa", s = "dog cat cat dog"
            Output: false

        Notes:
            - s contains only lowercase English letters and spaces.
            - s does not contain any leading or trailing spaces.
            - All the words in s are separated by a single space.
        """
        def map_to_int(string) -> list[int]:
            d = {}
            counter = 0
            for char in string:
                if char not in d:
                    d[char] = counter
                    counter += 1
            return [d[char] for char in string]
            
        return map_to_int(pattern) == map_to_int(s.split())


if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(sol.wordPattern(pattern, s))




