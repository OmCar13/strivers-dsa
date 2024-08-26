def sumOfAllDivisors(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                total_sum += j
                if j != i // j:
                    total_sum += i // j
    return total_sum