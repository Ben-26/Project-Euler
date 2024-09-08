"""
Derived formula for mxn grid as m(m+1)/2 * n(n+1)/2 
For fixed m solved for n to get bounds, +- L 

"""

def main():
    A = 0
    epsilon = float('inf')
    L = 10**6
    k = 8*10**6

    ubm = int(k**0.25)
    for m in range(1, ubm):
        a = (k - L) / (m * (m + 1))
        b = (k + L) / (m * (m + 1))


        lbn = int((-1 + (1 + 4 * a)**0.5) // 2)
        ubn = int((-1 + (1 + 4 * b)**0.5) // 2)
        
        for n in range(lbn, ubn):
            delta = abs(m * (m + 1) * n * (n + 1) - k)

            if delta < epsilon:
                print(f"m = {m}, n = {n} , delta = {delta // 4}")
                epsilon = delta
                A = m * n
    print(A)


    
if __name__ == "__main__":
    main()
