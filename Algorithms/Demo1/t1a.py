

def is_divisible_without_division(n: int, m: int):
    """
    Check if an integer is evenly divisible by another integer without using division.

    Parameters:
        n (int): The integer to be checked for divisibility.
        m (int): The integer by which to check divisibility.

    Returns:
        bool: True if 'n' is evenly divisible by 'm', False otherwise.

    Note:
        - If 'n' is 0, the function will always return True, as any number is evenly divisible by 0.
        - If 'm' is 0, the function will always return False, as division by zero is not allowed.
    """
    num1 = n
    num2 = m

    # Division by zero not allowed
    if num2 == 0:
        print("Division by zero not allowed, please try another number!")
        return False

    # One can check if n is divisible by m by subtracting m from n k times.
    # If num1 (n) becomes exactly 0, it means that num1 (n) is divisible by num2 (m).
    # In any other case, num1 (n) is not divisible by num2 (m).
    while num1 > 0:
        num1 -= num2

    if num1 == 0:
        return True
    else:
        return False


print(is_divisible_without_division(20, 3))    # False
print(is_divisible_without_division(25, 5))    # True
print(is_divisible_without_division(100, 20))  # True
print(is_divisible_without_division(31, 0))    # False
