class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        """
        Given an array of strings 'words', finds the words that can be
        typed using letters of the alphabet on only one row of an ANSI keyboard.

        Example:
            Input: words = ["Hello","Alaska","Dad","Peace"]
            Output: ["Alaska","Dad"]
        """
        keyboard_set = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []
        for word in words:
            word_set = set(word.lower())
            if any(word_set.issubset(row) for row in keyboard_set):
                result.append(word)
        return result


if __name__ == "__main__":
    sol = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(sol.findWords(words))