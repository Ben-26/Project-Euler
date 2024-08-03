from math import sqrt

def continued_fraction(n):
    mn = 0.0
    dn = 1.0
    F = [int(sqrt(n))]
    while F[-1] != 2 * F[0]:
        mn = dn * F[-1] - mn
        dn = (n - mn**2) / dn
        F.append(int((F[0] + mn) / dn))
    return F


def main():
    counter = 0
    for i in range(1, 10000):
        if int(sqrt(i))**2 != i:
            counter += len(continued_fraction(i)[1:]) % 2
    print(counter)

if __name__ == "__main__":
    main()