
"""
https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics) Roughly used to derive formula

Increasing numbers: 
n+9 C 9 - 1, subract 1 to ignore a number with n 0's

Decreasing numbers:
n+10 C10 - (n + 1), choose 10 as we are using {0, ... , 9} instead of {1, ... 9} in the increasing numbers
Subtract n+1 to account for 000 -> 1000, i.e. numbers with leading zeros that are missed

Constants are counted twice so we must remove 9n of them 

Giving the formula 
(n+9)C9 + (n+10)C10 - 10n - 2
"""
from math import comb

def main():
    lim = 100
    print(comb(lim + 9, 9) + comb(lim + 10, 10) - 10*lim - 2)

if __name__ == "__main__":
    main()

    
    
    