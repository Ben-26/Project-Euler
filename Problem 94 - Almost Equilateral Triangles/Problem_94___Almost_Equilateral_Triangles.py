"""
Herons formula 
with (a, a, a+1) -> A^2 = (3a + 1)(a - 1)(a + 1)^2 / 16 
with (a, a, a-1) -> A^2 = (3a + 1)(a + 1)(a - 1)^2 / 16

observe (3a + 1)(a^2 - 1) / 16


"""
from math import sqrt

## TOO SLOW
def main():
    
    perfect_squares = []
    j = 0
    while j**2 <= 10**18:
        perfect_squares.append(j**2)
        j += 1

    p_sum = 0
    
    for i in range(2, 10**9):
        base = (3 * i + 1) * (i ** 2 - 1) / 16
        A1 = base * (i + 1)
        
        if A1 in perfect_squares and 3 * i + 1 <= 10**9:
            p_sum += 3 * i + 1

        A2 = base * (i - 1)

        if A2 in perfect_squares and 3 * i - 1 <= 10**9:
            p_sum += 3 * i - 1

    print(p_sum)
        

if __name__ == "__main__":
    main()

