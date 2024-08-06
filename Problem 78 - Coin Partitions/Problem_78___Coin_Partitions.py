"""
Ref:
Using the recurrence relation from
https://en.wikipedia.org/wiki/Pentagonal_number_theorem 
"""

def pentagonal_number(k):
    return k * (3 * k - 1) // 2

def main():
    cache = [1]
    n = 1
    
    pentagonals = []
    sgn = []
    k = 1
    while True:
        p1 = pentagonal_number(k)
        p2 = pentagonal_number(-k)
        if p1 > 10**6 and p2 > 10**6:
            break
        pentagonals.append(p1)
        pentagonals.append(p2)
        sgn.append((-1) ** (k + 1))
        sgn.append((-1) ** (k + 1))
        k += 1
    
    while True:
        cache.append(0)
        for i in range(len(pentagonals)):
            p = pentagonals[i]
            if p > n:
                break
            cache[n] += sgn[i] * cache[n - p]
            cache[n] %= 10**6 
        
        if cache[-1] == 0:
            print(n)
            break
        
        n += 1

if __name__ == "__main__":
    main()
