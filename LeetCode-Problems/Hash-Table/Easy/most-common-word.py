from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        This method, given an input string ('paragraph') and a string array of the banned words ('banned'),
        finds the most frequent word that is not banned.

        Args:
            paragraph (str): The input string to be counted for the most frequent word.
            banned (list[str]): A string array containing the banned words.

        Returns:
            str: The most frequent word of the input string 'paragraph'.

        Notes:
            - At least one word in the input string 'paragraph' should not be banned.
            - The answer should be unique (i.e., only one non-banned word should appear more than others).
            - The words in paragraph are case-insensitive.
        """
        # Change the upper case letters of the paragraph into lower case letters
        paragraph = paragraph.lower()

        # Specify the characters that are used to split the paragraph
        split_chars = r"[.,:;'!? ]+"
        # In the regular expression r'[.,!? ]+', the 'r' before the pattern is a prefix indicating a "raw string".
        # A raw string is often used for regular expressions because it helps avoid issues with backslashes.
        # In a raw string, backslashes are treated as literal characters rather than escape characters.
        # [.,!?] --> inside the square brackets are all the characters that are used to split the paragraph.
        # + --> This is a quantifier that matches one or more occurrences of the preceding character class
        # (i.e., the characters inside the square brackets).

        # Use the re module to split the paragraph.
        # The reason one should use the re module instead of the str.split() function is that
        # re.split() accepts multiple seperators, whereas str.split() accepts only one seperator.
        splitted_paragraph = re.split(split_chars, paragraph)

        # filter(None, iterable) is used to filter out elements from the iterable
        # (in this case, the list of words obtained from the split operation)
        # that evaluate to False when passed to the bool function.
        splitted_paragraph = list(filter(None, splitted_paragraph))
        # An empty string evaluates to False in a boolean context, so it will be excluded from the result.

        # Remove the banned words from the paragraph
        final_paragraph = [word for word in splitted_paragraph if word not in banned]

        # Use Counter from collections to count the occurrences of the words
        words_count = Counter(final_paragraph)

        return max(words_count, key=lambda x: words_count[x])
        # Note: In the lambda expression, 'x' represents the keys (words) in words_count
        # --> words_count['key'] will return the value associated with that specific key
        # --> max() function will return the key associated with the highest value (most occurrences)


    # Uncommented version
    def mostCommonWord2(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        split_chars = r"[.,:;'!? ]+"
        splitted_paragraph = re.split(split_chars, paragraph)
        splitted_paragraph = list(filter(None, splitted_paragraph))
        final_paragraph = [word for word in splitted_paragraph if word not in banned]
        words_count = Counter(final_paragraph)
        return max(words_count, key=lambda x: words_count[x])



if __name__ == "__main__":
    sol = Solution()
    paragraph = "..Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(sol.mostCommonWord(paragraph, banned))
