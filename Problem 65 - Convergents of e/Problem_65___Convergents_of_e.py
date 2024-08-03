def simplify_continued_fraction(F):
    num = F[-1]
    denom = 1   
    for x in reversed(F[:-1]):
        num, denom = denom, num 
        num += x * denom 
    return [num, denom]

def main():
    e = [2] + [int(2 * (k + 1) / 3) if k % 3 == 2 else 1 for k in range(1, 100)]
    print(sum(int(digit) for digit in str(simplify_continued_fraction(e)[0])))


if __name__ == "__main__":
    main()