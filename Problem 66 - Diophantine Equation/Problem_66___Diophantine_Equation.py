from math import sqrt

"""
Ref:
Pell's equations PDF
https://en.wikipedia.org/wiki/Pell%27s_equation
https://mathworld.wolfram.com/PellEquation.html
"""

# Continued fraction of sqrt(x)
def continued_fraction(n):
    mn = 0.0
    dn = 1.0
    F = [int(sqrt(n))]
    while F[-1] != 2 * F[0]:
        mn = dn * F[-1] - mn
        dn = (n - mn**2) / dn
        F.append(int((F[0] + mn) / dn))
    return F

def simplify_continued_fraction(F):
    num = F[-1]
    denom = 1   
    for x in reversed(F[:-1]):
        num, denom = denom, num 
        num += x * denom 
    return [num, denom]

def main():
   largest_minimal = [0, 0]
   for D in range(1, 1001):
       if int(sqrt(D))**2 != D:
           F = continued_fraction(D)
           F = simplify_continued_fraction(F[:-1] if len(F) % 2 == 1 else F + F[1:-1])
           if F[0] > largest_minimal[0]:
               largest_minimal = [F[0], D]
   print(largest_minimal[1])   
   
if __name__ == "__main__":
    main()