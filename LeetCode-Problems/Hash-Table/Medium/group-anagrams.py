class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Given an array of strings, group the anagrams together.
        An anagram is a word or phrase formed by rearraging the letters of a different word or phrase

        Args:
            strs (list[str]): A list of strings.

        Returns:
            list[list[str]]: A list containing groups of anagrams.
            Each group is represented as a list of strings.

        Examples:
            sol = Solution()
            sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
                --> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        # Create an empty dictionary to store the key-value pairs
        d = {}
        for word in strs:
            # To get the unique keys to group the anagrams,
            # one can use the sorted() method together with the join() method.
            # sorted() first creates a list consisting of the individual letters of the word
            # in alphabetical order (e.g., sorted("cat") --> ["a", "c", "t"]),
            # then the join() method concatenates the letters back together
            # (""join.(["a", "c", "t"] --> "act")
            sorted_word = "".join(sorted(word))
            if sorted_word not in d:
                # If the key (sorted_word) is not yet initialized into the dictionary,
                # initialize its value as an empty list.
                d[sorted_word] = []
                # append the unordered original word to the list
                d[sorted_word].append(word)
            else:
                # If the key is already in the dictionary, append its anagram to it.
                d[sorted_word].append(word)
        # Since the function needs to return a nested list,
        # one can use e.g. list comprehension on d.values().
        # Note that each value is already its own list,
        # so using list comprehension on the values will return a nested list.
        return [l for l in d.values()]


    # Uncommented version
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = []
                d[sorted_word].append(word)
            else:
                d[sorted_word].append(word)
        return [l for l in d.values()]


if __name__ == "__main__":
    sol = Solution()
    l1 = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(sol.groupAnagrams(l1))

