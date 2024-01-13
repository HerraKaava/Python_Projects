class Solution:
    def fibonacci(self, n: int) -> int:
        """
        Finds the nth Fibonacci number.
        The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
        Starting from 0 and 1, the sequence begins
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            i = 0    # Helper for the loop
            k = 0    # First Fibonacci number
            c = 1    # Second Fibonacci number
            z = k + c
            # The first two cases are handled outside the loop,
            # So the loop needs to iterate n-2 times to get to the nth Fibonacci number.
            while i < n-2:
                k = c
                c = z
                z = k + c
                i += 1
            return z

    def fib_recursive(self, n: int) -> int:
        """
        Find the nth Fibonacci number using recursion.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            # F_n = F_{n-1} + F_{n-2}
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fibonacci(19))        # 4181
    print(sol.fib_recursive(19))    # 4181