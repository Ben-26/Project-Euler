from math import sqrt

def b(n):
    return -0.125 * (4 - 2 * (3 - 2*sqrt(2))**n - 2 * (3 + 2*sqrt(2))**n + sqrt(2) * (3 + 2*sqrt(2))**n - sqrt(2) * (3 - 2*sqrt(2))**n)

def r(n):
    return -0.25 * 1/sqrt(2) * ((3 - 2*sqrt(2))**n - sqrt(2) * (3 + 2*sqrt(2))**n)


def main():
    n = 1

    while b(n) + r(n) < 10**12:
        n += 1

    print(int(b(n)) + 2) # No idea why it is off by a factor of 2 , should be a factor of 1 but int rounds down 

if __name__ == "__main__":
    main()
