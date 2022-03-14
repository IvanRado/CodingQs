# Given an integer n, return the number of prime numbers that are strictly less than n.
# Straightforward solution
# Time Complexity: O(n * p), Space Complexity: O(p)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n <= 3:
            return 1
        
        count_primes = 2
        primes = [2, 3]
        for i in range(3, n):
            divisible = False
            for divisor in primes:
                if i % divisor == 0:
                    divisible = True
                    break
            if divisible:
                continue
            else:
                primes.append(i)
                count_primes += 1
                
        return count_primes
            
# Sieve of Eratosthenes
class Solution(object):
    def countPrimes(self, n: int) -> int:
        # Early exit for numbers less than 2
        if n < 2: 
            return  0
        # Create a strike list for the input range, initializing all indices to prime (1)
        strikes = [1] * n

        # Know 0 and 1 aren't prime
        strikes[0], strikes[1] = 0, 0

        # Set multiples of remaining markers that are marked as prime to not prime.
        # It is safe to ignore numbers already marked as not prime because there are
        # factors that divide evenly into this number and all its multiples. Use upper limit
        # of (n**0.5) + 1 because:
        # 1) Smallest factor of a non-prime number will not be > sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if strikes[i] != 0:
                strikes[i*i:n:i] = [0] * ((n-1-i*i)//i+1)

        return sum(strikes)

        