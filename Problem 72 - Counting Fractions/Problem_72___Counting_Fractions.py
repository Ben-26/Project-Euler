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
    return int(cache)


def main():
    print(sum(euler_totient(d) for d in range(2, 10**6+1)))

if __name__ == "__main__":
    main()
