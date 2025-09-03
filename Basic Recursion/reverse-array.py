def reverse(arr: list) -> list:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_recursive(arr: list, left: int, right: int) -> list:
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse_recursive(arr, left + 1, right - 1)

print(reverse(reverse_recursive([1, 2, 3, 4, 5], 0, 4)))  # Output: [5, 4, 3, 2, 1]
print(reverse_recursive(reverse([1, 2, 3, 4, 5, 6]), 0, 5))  # Output: [6, 5, 4, 3, 2, 1]