class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        """
        Given an integer 'num', finds three consecutive integers
        (as a sorted array) that sum to num.
        If 'num' cannot be expressed as the sum of three consecutive integers,
        an empty array will be returned instead.

        Examples:
            Input: num = 33
            Output: [10,11,12]
            Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
        """
        # The sum of three consecutive numbers can be written as n+(n+1)+(n+2),
        # which clearly is the same as 3n+3.
        # If there exists numbers n, n+1, n+2 such that they equal to some number k,
        # the first number n can be solved from equation 3n+3 = k  <-->  n = (k-3)/3

        n = (num-3) // 3
        if n + (n+1) + (n+2) == num:
            return [n, n+1, n+2]
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfThree(33))