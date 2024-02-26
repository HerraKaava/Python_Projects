class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Find if the two input strings s and t are anagrams or not.

        An Anagram is a word formed by rearranging the letters of a different word,
        typically using all the original letters exactly once.
        """
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagrama"
    print(sol.isAnagram(s, t))
