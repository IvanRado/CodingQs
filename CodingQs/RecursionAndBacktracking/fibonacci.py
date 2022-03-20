# Implement Fibonacci sequence
# Given n, return the nth number of the fibonacci sequence

def fibonacciRecursive(n: int):
    if n <= 2:
        return 1
    
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    

def fibonacciIterative(n: int):
    if n <= 2:
        return 1

    n1, n2 = 1, 1
    for _ in range(n-2):
        res = n1 + n2
        n1 = n2
        n2 = res

    return n2
    
def fibonacciMemoization():
    cache = {}
    def fib(n: int):
        if n in cache.keys():
            return cache[n]
        else:
            if n <= 2:
                return 1
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]

    
    return fib


x = fibonacciRecursive(10)
y = fibonacciIterative(10)
fibs = fibonacciMemoization()
z = fibs(10)

print(f"Fibonacci found iteratively: {x}")
print(f"Fibonacci found recursively: {y}")
print(f"Fibonacci found with memoization: {z}")