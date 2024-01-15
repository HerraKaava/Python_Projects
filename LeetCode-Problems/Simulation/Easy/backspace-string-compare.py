class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Finds if two strings, s and t, are equal when both are typed into empty text editors.

        Notes:
            - This function treats '#' as a backspace character.
            -  If backspacing an empty string, the string will remain empty.

        Examples:
            Input: s = "ab#c", t = "ad#c"
            Output: true
            Explanation: Both s and t become "ac".

            Input: s = "a#c", t = "b"
            Output: false
            Explanation: s becomes "c" while t becomes "b".
        """
        def use_backslash(string: str) -> str:
            new_string = []
            for char in string:
                if char != '#':
                    new_string.append(char)
                elif char == '#':
                    if new_string:
                        new_string.pop()
            return ''.join(new_string)

        return use_backslash(s) == use_backslash(t)


if __name__ == "__main__":
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    s2 = "ab##"
    t2 = "a#b#"
    s3 = "##"
    t3 = "#"
    print(sol.backspaceCompare(s, t))
    print(sol.backspaceCompare(s2, t2))
    print(sol.backspaceCompare(s3, t3))


