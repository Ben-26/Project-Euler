"""
NW: 4n^2 + 1
NE: 4n^2 - 2n + 1
SW: 4n^2 + 2n + 1
SE: (2n-1)^2 
"""

def is_prime(x):
    if (x == 2):
        return 1
    if (x < 2 or x % 2 == 0):
        return 0
        
    i = 3
    while (i*i <= x):
        if(x % i == 0):
            return 0
        i+=2
    return 1


if __name__ == "__main__":
    primes = 0
    total = 1
    
    n = 1
    side_length = 1
    while primes / total > 0.1 or primes / total == 0:
        alpha = 4 * n**2 + 1
        primes += is_prime(alpha)
        primes += is_prime(alpha + 2 * n)
        primes += is_prime(alpha - 2 * n)
        total += 4
        #print(f"there are {primes} primes and {total} total")
        n += 1
    print(2 * n - 1)
    