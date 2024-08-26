"""
In short generate a list of primes less than a big enough number (I started with 10,000,000),
filter that list to include only primes which have 3 repeated digits, then go through your new 
list and replace the 3 times repeated digit to every digit (Use the str.replace() function in 
python for this!), check if it's prime, if you find a family of 8 stop.
From https://www.ivl-projecteuler.com/overview-of-problems/15-difficulty/problem-51
"""

from math import sqrt

def generate_prime_sieve(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(sqrt(n)) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def is_prime(n):
    if n == 2 or n == 3:
        return True
    
    if n < 2 or n % 2 == 0:
        return False
    
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
      
def main():
    primes = [i for (i, isprime) in enumerate(generate_prime_sieve(10**6)) if isprime]
    filtered = []
    
    for p in primes:
        for c in range(0,10):
            if str(p).count(str(c)) == 3:
                filtered.append([p,c])
    for p in filtered:
        count = 0
        for c in range(0,10):
            temp = str(p[0]).replace(str(p[1]),str(c),3)
            if temp[0] == "0":
                pass
            elif is_prime(int(temp)):
                count += 1
        if count == 8:
            print(p[0]) 
            break

if __name__ == "__main__":
    main()      

