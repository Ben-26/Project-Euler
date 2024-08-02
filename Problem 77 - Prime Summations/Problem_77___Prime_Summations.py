def generate_primes(p_max):
    def prime(x):
        if x == 2:
            return True
        if (x < 2 or x % 2 == 0):
            return False

        i = 3
        while (i * i <= x):
            if (x % i == 0):
                return False
            i += 2
        return True
    
    primes = []
    for i in range(2, p_max):
        if prime(i):
            primes.append(i)
    return primes


def main():
    p_max = 1000
    primes = generate_primes(p_max)
    cache = [0] * (p_max + 1)
    cache[0] = 1

    
    for prime in primes:
        for j in range(prime, p_max + 1):
            cache[j] += cache[j - prime]
    
    i = 0
    while cache[i] < 5000:
        i += 1
        
    print(i)
   
   
if __name__ == "__main__":
    main()