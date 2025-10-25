import math
def count_digits(n: int) -> int:
    """Count the number of digits in a given integer n.

    Args:
        n (int): The non-negetive integer whose digits are to be counted.
    returns:
        int: The number of digits in the integer n.
    """
    if  n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0: return 1
    return int(math.log10(n)) + 1

print(count_digits(0))
print(count_digits(1))
print(count_digits(12345))
print(count_digits(1234567890))
print(count_digits(-12345))