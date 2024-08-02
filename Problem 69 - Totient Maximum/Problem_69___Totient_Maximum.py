from math import gcd

def euler_totient(n):
    if n == 1:
        return 1
    
    def factorise(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    
    factors = factorise(n)
    cache = n
    
    for p in factors:
        cache *= (1 - 1 / p)
    return cache


def main():
    maximum = [1, 1]
    for i in range(2, 10**6):
        ratio = i / euler_totient(i)
        if ratio > maximum[0]:
            maximum = [ratio, i]
    print(maximum[1])

if __name__ == "__main__":
    main()