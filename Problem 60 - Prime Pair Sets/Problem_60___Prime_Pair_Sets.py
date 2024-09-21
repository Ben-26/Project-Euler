

def generate_prime_sieve(n):
    bool_primes = [True] * (n + 1)
    bool_primes[0] = bool_primes[1] = False
    for i in range(int(n**0.5) + 1):
        if bool_primes[i]:
            for j in range(i * i, n + 1, i):
                bool_primes[j] = False            
    primes = [i for (i, is_prime)  in enumerate(bool_primes) if is_prime]
    return [3] + primes[3:]   # Removing 2 and 5, ending with 2 -> even, ending with 5 -> multiple of 5

N = 10000
primes = generate_prime_sieve(N) 

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    
    if n < N:
        return n in primes
    else:
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

def main():
    primePair = lambda a, b:  is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))
    primePairSet = lambda arr: all([primePair(p, arr[-1]) for p in arr[:-1]])
    
    best_sum = float("inf")

    for p1 in primes:
        for p2 in primes[primes.index(p1) + 1:]:
            c = [p1, p2]
            if primePairSet(c):
                for p3 in primes[primes.index(p2) + 1:]:
                    if primePairSet(c + [p3]):
                        c.append(p3)
                        for p4 in primes[primes.index(p3) + 1:]:
                            if primePairSet(c + [p4]):
                                c.append(p4)
                                for p5 in primes[primes.index(p4) + 1:]:
                                    if primePairSet(c + [p5]):
                                        c.append(p5)
                                        if sum(c) < best_sum:
                                            best_sum = sum(c)
                                            print(f"New best = {best_sum} from {c}")
                                        
    print(best_sum)

if __name__ == "__main__":
    main()  
