class Solution:
    def fib(self, n: int) -> int:
        """
        Finds the nth Fibonacci number.
        The Fibonacci sequence is a sequence in which
        each number is the sum of the two preceding ones.

        Starting from 0 and 1, the sequence begins
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
        """
        if n <= 1:
            return n
        n1, n2 = 0, 1   # F(0), F(1)
        for _ in range(2, n+1):
            F = n1 + n2
            n1 = n2
            n2 = F
        return F


if __name__ == "__main__":
    sol = Solution()
    n = 19
    print(sol.fib(n))
