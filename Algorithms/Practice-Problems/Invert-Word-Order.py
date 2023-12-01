

def invert_word_order(input_str):
    """
    Inverts the order of words in the input string without using
    built-in string handling functions such as split, join or strip.

    Args:
        input_str (str): The input string containing words to be inverted.

    Returns:
        str: A new string with the order of words inverted.

    Example:
        original_string = "I love programming"
        invert_word_order(original_string)
        output: "programming love I"
    """
    # Remove the possible space characters before and after the word
    # e.g. ("  I love programming   " --> "I love programming")
    # Note that the removing part is not done here.
    # In this part, I am finding the boundaries where the actual words start.
    start = 0
    while start < len(input_str) and input_str[start] == " ":
        start += 1
    end = len(input_str) - 1
    while end >= 0 and input_str[end] == " ":
        end -= 1
    # These 'start' and 'end' variables are going to be used in the loop
    # to set the boundaries for from which index to start the iteration,
    # and to which index stop the iteration
    # (so that the white spaces from the start and from the end gets excluded)

    char_list_nested = []    # This list holds all the characters of the words as a nested list
    char_list_temp = []      # This list temporarily hold the characters of the current word
    # Iterate through the characters (within the boundaries obtained earlier) in reversed order
    for i in range(end, start - 1, -1):
        if input_str[i] == " " and len(char_list_temp) > 0:
            char_list_nested.append(char_list_temp)
            char_list_temp = []
            continue
        if input_str[i] != " ":
            char_list_temp.append(input_str[i])
    char_list_nested.append(char_list_temp)
    # Note that after this loop, the characters of the words in the char_nested_list are in reversed order.
    # e.g. if input_str = "I love programming", it has been stored as:
    # [['g', 'n', 'i', 'm', 'm', 'a', 'r', 'g', 'o', 'r', 'p'], ['e', 'v', 'o', 'l'], ['I']]

    # Since the characters are now in the right places, but still in reversed order,
    # to get them in the right order, one has to iterate through the characters once again in reversed order.
    str_new = ""    # This string is used to construct the new inverted word
    for index, word in enumerate(char_list_nested):
        for i in range(len(word)-1, -1, -1):
            str_new += word[i]
        if index < len(char_list_nested)-1:
            str_new += " "
    # The logic of the loop above:
    # After a list of the nested list has been iterated through,
    # a word has been succesfully added to the 'str_new' string.
    # After this, a white space is needed.
    # To avoid adding a trailing white space after the final iteration,
    # a condition can be added that checks whether the index of the current word is less than
    # the length of char_list_nested (which represents how many different words input_str contains).
    # Note that enumerate() starts indexing from zero.

    return str_new


# Uncommented version:
def invert_word_order2(input_str):
    start = 0
    while start < len(input_str) and input_str[start] == " ":
        start += 1
    end = len(input_str) - 1
    while end >= 0 and input_str[end] == " ":
        end -= 1

    char_list_nested = []
    char_list_temp = []
    for i in range(end, start - 1, -1):
        if input_str[i] == " " and len(char_list_temp) > 0:
            char_list_nested.append(char_list_temp)
            char_list_temp = []
            continue
        if input_str[i] != " ":
            char_list_temp.append(input_str[i])
    char_list_nested.append(char_list_temp)

    str_new = ""
    for index, word in enumerate(char_list_nested):
        for i in range(len(word) - 1, -1, -1):
            str_new += word[i]
        if index < len(char_list_nested) - 1:
            str_new += " "

    return str_new


if __name__ == "__main__":
    word1 = "I love programming"
    word2 = "  I love programming    "
    word3 = "   I    love    programming     "
    print(invert_word_order(word1))    # programming love I
    print(invert_word_order(word2))    # programming love I
    print(invert_word_order(word3))    # programming love I
