# print all binary strings of length n such that there are no consecutive 1's
def print_binaryStrings(n: int, curr: str = "") -> None:
    if n == 0:
        print(curr)
        return
    print_binaryStrings(n-1, curr + "0")
    if curr.endswith("0") or curr == "":
        print_binaryStrings(n-1, curr + "1")

print_binaryStrings(3)