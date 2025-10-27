import math

def reverse_a_number(num: int) -> int:
    """
    This function takes an integer number as input and returns the number with its digits reversed.
    
    Parameters:
    num (int): The integer number to be reversed.
    
    Returns:
    int: The reversed integer number.
    """
    # Convert the number to string, reverse it and convert back to integer
    reversed_num = 0
    sign = -1 if num < 0 else 1
    num = abs(num)
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num * sign


print(reverse_a_number(12345))
print(reverse_a_number(-12304500))
