# A function that returns the factorial 
# Both iterative and recursive cases


def findFactorialRecursive(n: int):
    if n == 1:
        return 1

    return findFactorialRecursive(n-1) * n

def findFactorialIterative(n: int):
    result = n
    for i in range(n-1, 0, -1):
        result *= i

    return result

x = findFactorialIterative(2)
y = findFactorialRecursive(2)

print(f"Factorial found iteratively: {x}")
print(f"Factorial found recursively: {y}")