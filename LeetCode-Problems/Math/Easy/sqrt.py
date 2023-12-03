class Solution:
    def mySqrt(self, a: int):
        """
        Given a non-negative integer a,
        return the square root of a rounded down to the nearest integer
        without using built-in exponent function or operator.

        Args:
            a (int): The non-negative integer to be squared

        Returns:
            int: The square root of a rounded down to the nearest (non-negative) integer.

        This can be solved using the Babylonian method.
        The idea of the Babylonian method is that for any number x:

            x * (a/x) = a = sqrt(a) * sqrt(a).

        From this it can be seen that if x is less than sqrt(a),
        then (a/x) has to be bigger than sqrt(a) to make up for it:

            if x < sqrt(a), then (a/x) > sqrt(a).

        The same goes other way around:

            if x > sqrt(a), then (a/x) < sqrt(x).

        --> Take the average of the two.

        x_{n+1} = (x_{n} + (a/x_{n}))/2 = (x_{n}^2 + a)/(2*x_{n})

        Hence, the Babylonian method (also known as Heron's method)
        is an iterative algorithm for approximating the square root of a number.

        The steps include:
            1. Start with an initial guess
            2. Iteratively improve the guess
            3. Check for "close enough"
            4. Round the result
        """
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number")

        # Initial guess
        x = a
        # Accuracy level
        epsilon = 0.000001

        while abs(x * x - a) > epsilon:
            x = (x + (a/x))/2    # Improve the guess
        return int(x // 1)       # Integer division (e.g., 11.6 // 1 --> 11)


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(49))    # 7
    print(sol.mySqrt(100))   # 10
    print(sol.mySqrt(187))   # 13

