def find_pairs_with_sum(numbers: list[int], target: int) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            n1, n2 = numbers[i], numbers[j]
            if n1 + n2 == target:
                pairs.append((n1, n2))
