def generate_primes_sieve(maximum):
    sieve = [True] * maximum
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(maximum**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, maximum, start):
                sieve[multiple] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    print(f"There are {len(primes)} primes below {maximum}")
    return primes


def main():
    upper_bound = 5*(10**7)
    primes = generate_primes_sieve(upper_bound)
    square_primes = []
    cube_primes = []
    quartic_primes = []
    for p in primes:
        sqr = p**2
        if sqr < upper_bound:
            square_primes.append(sqr)
        if sqr*p < upper_bound:
            cube_primes.append(sqr*p)
        if sqr**2 < upper_bound:
            quartic_primes.append(sqr**2)
    
    print(len(square_primes), len(cube_primes), len(quartic_primes))

    sums = set()
    for q in quartic_primes:
        for c in cube_primes:
            if q + c < upper_bound:
                for s in square_primes:
                    scq = s + c + q
                    if scq < upper_bound:
                        sums.add(scq)
    print(len(sums))   
    
if __name__ == "__main__":
    main()
