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
        least_idx_sum = float('inf')
        d = {}
        for s in list1:
            if s in list2:
                idx_sum = list1.index(s) + list2.index(s)
                if idx_sum <= least_idx_sum:
                    d[s] = idx_sum
                    least_idx_sum = idx_sum
        min_idx = min(d.values())
        return [key for (key, val) in d.items() if val == min_idx]


if __name__ == "__main__":
    sol = Solution()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(sol.findRestaurant(list1, list2))
