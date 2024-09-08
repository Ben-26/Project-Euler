from math import e


def generate_prime_sieve(n):
    bool_primes = [True] * (n + 1)
    bool_primes[0] = bool_primes[1] = False
    for i in range(int(n**0.5) + 1):
        if bool_primes[i]:
            for j in range(i * i, n + 1, i):
                bool_primes[j] = False            
    primes = [i for (i, is_prime)  in enumerate(bool_primes) if is_prime]
    return [3] + primes[3:]   # Removing 2 and 5, ending with 2 -> even, ending with 5 -> multiple of 5

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    N = 674
    primes = generate_prime_sieve(N) 
    


    
    



if __name__ == "__main__":
    main()  
