## List of 4 digit primes -> Digitise -> Permutate 4 digits -> Prime check -> Sequence check 
from math import log10, floor

def is_prime(x):
    if (x == 2):
        return True
    if (x < 2 or x % 2 == 0):
        return False
        
    i = 3
    while (i*i <= x):
        if(x % i == 0):
            return False
        i+=2
    return True

def fourDigitPermutator(x):
    return x

def seqCheck(x):
    if x[2] - x[1] == x[1] - x[0]:
        print(x)
    return True

def digitise(x):
    digits = [0]*(floor(log10(x)) + 1)
    for i in range(0, floor(log10(x)) + 1):
        digits[-1 * (i + 1)] = x % 10**i
        x = x - digits[-1 * (i + 1)]
    return digits

if __name__ == "__main__":
    primes = []
    for i in range(1001, 9999):
        if is_prime(i):
            primes.append(i)
    for p in primes:
        continue
    

# Calculates a^k ( mod n )
def modulo(a, k, n):
    if a < n:
        return a
    elif a == n:
        return 0
    else:
        return 
            
