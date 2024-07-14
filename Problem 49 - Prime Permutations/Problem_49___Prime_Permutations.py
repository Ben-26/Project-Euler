## List of 4 digit primes -> Sequence check -> Prime check -> Perm check 

#from math import log10, floor

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
  
if __name__ == "__main__":
    primes = []
    for i in range(1001, 9999):
        if is_prime(i):
            primes.append(i)
    for p in primes:
        for i in range(1, 4500):
            if p - i in primes and p + i in primes:
                if sorted(map(int, str(p - i))) == sorted(map(int, str(p))) and sorted(map(int, str(p - i))) == sorted(map(int, str(p + i))):
                    print(f"{[p-i, p, p+i]} : {str(p-i) + str(p) + str(p + i)}")
                
    
            
