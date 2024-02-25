from collections import Counter

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """
        Given two arrays of strings list1 and list2,
        finds the common strings with the least index sum.

        A common string with the least index sum is a common string such that
        if it appeared at list1[i] and list2[j] then i + j should be the
        minimum value among all the other common strings.

        If there is many common strings with the least index sum,
        all of them will be returned.

        Notes:
            - All the strings of list1 are unique.
            - All the strings of list2 are unique.
            - There must be at least one common string between list1 and list2.
        """
        intersection = set(list1) & set(list2)
        d = {}
        for word in intersection:
            d[word] = list1.index(word) + list2.index(word)
        return [key for (key, val) in d.items() if val == min(d.values())]


if __name__ == "__main__":
    sol = Solution()
    list1 = ["happy","sad","good"]
    list2 = ["sad","happy","good"]
    print(sol.findRestaurant(list1, list2))
