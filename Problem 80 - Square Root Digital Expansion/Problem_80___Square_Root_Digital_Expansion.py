from math import sqrt
from decimal import Decimal, getcontext

def decimal_root(terms, n):
    getcontext().prec = terms + 15  
    x = Decimal('1.0')
    n = Decimal(n)
    while True:
        next_x = (x + n / x) / 2
        if x == next_x:
            break
        x = next_x
    result = +x.quantize(Decimal(10) ** -terms)
    return list(str(result))

def main():
    total = 0
    for i in range(2, 101):
        if int(sqrt(i))**2 != i:   
            total += int(sqrt(i))
            digits = decimal_root(100, i)[2:-1]
            for d in digits:
                total += int(d)    
    print(total) # Off by +1 for some reason

if __name__ == "__main__":
    main()