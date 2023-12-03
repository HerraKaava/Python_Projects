class Solution:
    def isPowerOfTwo(self, n: int):
        """
        Determine if the given integer n is a power of two.
        An integer n is a power of two, if there exists an integer x such that n = 2^x

        Args:
            n (int): The integer to be checked.

        Returns:
            True if n is a power of two, false otherwise.
        """
        if n == 1:
            return True
        x = 1
        while True:
            x *= 2
            if x == n:
                return True
            if x > n:
                return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(16))       # 2^4 = 16 --> True
    print(sol.isPowerOfTwo(32768))    # 2^15 = 32768 --> True
    print(sol.isPowerOfTwo(15))       # False
    print(sol.isPowerOfTwo(1))        # 2^0 = 1 --> True
