from math import gcd

def gen_triples(N):
    triples = []
    for m in range(2, int((N//2)**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if c < N:
                    k = 1
                    while k * (a + b + c) < N:
                        triples.append((k * a, k * b, k * c))
                        k += 1
    return triples

def main():
    triples = gen_triples(1500000) 

    perim = {}
    for t in triples:
        p = sum(t)
        if p < 1500000:
            if p in perim:
                perim[p] += 1
            else:
                perim[p] = 1

    counter = 0    
    for p in perim:
        counter += (perim[p] == 1)
    print(counter)

if __name__ == "__main__":
    main()
