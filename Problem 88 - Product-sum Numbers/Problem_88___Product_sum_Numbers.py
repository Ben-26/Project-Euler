from typing import List

def unique_factors(n: int) -> List[List[int]]:
        def dfs(target, start_factor):
            if memo:
                factors.append(memo + [target])
            f = start_factor
            while f * f <= target:
                if target % f == 0:
                    memo.append(f)
                    dfs(target // f, f)
                    memo.pop()
                f += 1

        memo = [] # Current list 
        factors = []
        dfs(n, 2)
        return factors


def main():
    nmax = 12000

    l = [0] * (nmax + 1) # idx = chain length 
    u = 0 # Updates

    n = 2
    while u < nmax - 2:
        unqf = unique_factors(n) # Generate all possible sums of divisors of n 
        for f in unqf:
            k = n - sum(f) + len(f)
            if k < nmax and not l[k]:
                l[k] = n
                u += 1
        n += 1
    print(sum(set(l)))


if __name__ == "__main__":
    main()
    


