"""For 1 <= n <= 100
We know the choose function is symmetric. That is 
nCr = nC(n-r)
1 <= r <= floor(n/2) -> add 2 to counter every true
to avoid the duplication of the odd n's a single count - not working , misses numbers
"""
from math import floor, factorial

def nCr(n, r):
    return int(factorial(i) / (factorial(r) * factorial(n - r)))

if __name__ == "__main__":
    counter = 0
    for i in range(1, 101):
        for r in range(0, i):
            if nCr(i, r) > 10**6:
                counter = counter + 1
    print(counter)
    
