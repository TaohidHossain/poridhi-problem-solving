from typing import List

def extractDigit(n: int) -> List[int]:
    """
    Question: Extract digits from a number

    input: n IS non negetive integer
    output: digits is a list of digits extracted from n
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    digits: List[int] = []
    while n!=0:
      digits.append(n%10)
      n = int(n/10)  

    digits.reverse()
    return digits

print(extractDigit(1234))
print(extractDigit(4321))
print(extractDigit(1000000))
print(extractDigit(482753855832757))
print(extractDigit(0))
print(extractDigit(1))
print(extractDigit(-13))
