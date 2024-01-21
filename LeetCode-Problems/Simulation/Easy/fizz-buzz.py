class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        Given an integer n, return a string array answer (1-indexed) where:
        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.
        """
        result = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(3))
