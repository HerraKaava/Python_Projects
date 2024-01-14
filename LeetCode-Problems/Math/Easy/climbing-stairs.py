class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Finds the number of distinct ways one can climb n steps,
        when each time one can either climb 1 or 2 steps.

        Notes:
            - This problem can be solved by finding the (n+1)th Fibonacci number.
        """
        i = 0
        n1 = 0
        n2 = 1
        f_n = n1 + n2
        while i < n-1:
            n1 = n2
            n2 = f_n
            f_n = n1 + n2
            i += 1
        return f_n


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(18))    # 4181