def euler_totient(n):
    if n == 1 or n == 2:
        return 1
    
    def prime(x):
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
    
    while n % 2 == 0:
        n //= 2

    if prime(n):
        return n - 1
    else:    
        factors = factorise(n)
        cache = n
    
        for p in factors:
            cache *= (1 - 1 / p)
        return int(cache)

def main():
    totient_ratio = 10**10
    n = 1;
    for i in range(2, 10**7):
        totient = euler_totient(i)
        if sorted(list(str(i))) == sorted(list(str(totient))):
            if i / totient < totient_ratio:
                totient_ratio = i / totient
                n = i
                print(f"New minimum totient ratio {totient_ratio} at n = {n}")
                
    print(n)

if __name__ == "__main__":
    main()