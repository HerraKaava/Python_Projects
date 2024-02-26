class Solution:
    def addDigits(self, num: int) -> int:
        """
        Given an integer num, repeatedly adds all its digits until the result has only one digit.

        Examples:
            Input: num = 38
            Output: 2
            Explanation: The process is
            38 --> 3 + 8 --> 11
            11 --> 1 + 1 --> 2
            Since 2 has only one digit, return it.

            Input: num = 0
            Output: 0
        """
        def sum_digits(num):
            """
            This function calls itself recursively until the length of 'num'
            (in string format) is equal to 1.
            """
            num_to_str = str(num)
            if len(num_to_str) == 1:
                return num
            s = sum(int(i) for i in num_to_str)
            return sum_digits(s)

        return sum_digits(num)


    def add_digits(self, num:int) -> int:
        """
        Another implementation.
        This function is more efficient memory-wise than the one above.
        """
        if num <= 1:
            return num

        def add(num):
            result = 0
            digit_list = list(str(num))
            while digit_list:
                result += int(digit_list.pop())
            return result

        sum_digits = add(num)
        while len(str(sum_digits)) > 1:
            sum_digits = add(sum_digits)

        return sum_digits


if __name__ == "__main__":
    sol = Solution()
    num = 38
    print(sol.addDigits(num))
