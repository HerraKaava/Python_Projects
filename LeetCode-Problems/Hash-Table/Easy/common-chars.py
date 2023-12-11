from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        Given a string array 'words', finds all characters that show up in all strings
        within the words (inlcuding duplicates).

        Args:
            list[str]: The string array to be checked

        Returns:
            list[str]:

        Examples:
            Input: words = ["bella","label","roller"]
            Output: ["e","l","l"]

            Input: words = ["cool","lock","cook"]
            Output: ["c","o"]
        """
        # Use Counter from colletions to get the character counts for the first word
        char_count = Counter(words[0])

        # Update char_count by finding the common characters in the rest of the words
        for word in words[1:]:
            # Update char_count by finding the intersection of the words
            # (i.e., the letters that appear in all of the words)
            # Example:
            # Counter('bella') --> Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
            # then after updating the Counter with the intersection of "le" --> Counter({'e': 1, 'l': 1}).
            # This is because 'e' and 'l' are the only letters that appear in both 'bella' and 'le'.
            # Intersection can be found using the "&=" operator.
            char_count &= Counter(word)

        return [char for char, count in char_count.items() for _ in range(count)]

        # The logic of the list comprehension above:

            # 'char_count.items()' iterates over the key-value pairs of the Counter,
            # where the key is the character, and the value is the count of that character.

            # 'for char, count in char_count.items()' unpacks these key-value pairs into 'char' and 'count'.

            # 'for _ in range(count)' is a nested loop. It repeats the character 'count' times.


    # Uncommented version
    def commonChars2(self, words: list[str]) -> list[str]:
        char_count = Counter(words[0])
        for word in words[1:]:
            char_count &= Counter(word)
        return [char for char, count in char_count.items() for _ in range(count)]


if __name__ == "__main__":
    sol = Solution()
    words = ["bella", "label", "roller"]
    print(sol.commonChars(words))    # ['e', 'l', 'l']