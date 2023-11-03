

def count_consecutive_chars(input_string):
    """
    Count the number of consecutive identical characters at the beginning of a string.

    Args:
        input_string (str): The input string in which consecutive characters will be counted.

    Returns:
        int: The count of consecutive identical characters at the beginning of the string.
    """
    # A helper variable to keep track of the count of the consecutive characters
    # (the count obviously has to start from 1).
    char_count = 1
    # Notice that the range needs to go from 0 to len(input_str)-1.
    # This is because the algorithm compares the previous character to the next character.
    # If the loop ranged from 0 to len(input_str), one would get an index out of range error.
    # For example, if input_str = "hello" --> len(input_str) == 5.
    # input_str[5+1] would produce an index out of range error.
    # i.e. to compare every letter in the input string, the algorithm only needs to go from 0 to len(input_str)-1.
    for i in range(len(input_string)-1):
        if input_string[i] == input_string[i+1]:
            char_count += 1
        else:
            return char_count
            # This return call breaks the streak and returns the char_count.
            # Notice that without this return call, the string 'aabaa', for example, \
            # would not return 2 as one would expect, but rather 4,
            # because the logic of the algorithm is designed such that every consecutive character \
            # (e.g. aa, bb, cc) increases the value of the char_count variable.

    return char_count
    # This return call is necessary because if every character in the input string are the same,
    # (e.g., input_str = 'zzz'), the function would return none without this return call.
    # This is because the other return call is called if and only if the streak breaks.


print(count_consecutive_chars('aaaabaaaaaaaa'))    # 4
print(count_consecutive_chars('abcabc'))           # 1
print(count_consecutive_chars('zzz'))              # 3
