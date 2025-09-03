def print_combinations(elements: list, idx: int = 0, sub: list = []) -> None:
    if idx == len(elements):
        print(sub)
        return
    
    curr = elements[idx]
    sub.append(curr)
    print_combinations(elements, idx + 1, sub)
    sub.pop()
    print_combinations(elements, idx + 1, sub)


print_combinations(['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5])
