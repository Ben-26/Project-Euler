import numpy as np

def main():
    U = lambda n: sum((-n)**i for i in range(0, 11))
    BOP = lambda n, coeff: sum(coeff[i] * n**i for i in range(0, len(coeff)))
    
    M = np.zeros((10, 10))
    for i in range(0, 10):
        for j in range(0, 10):
            M[i, j] = (i+1)**j

    fit = 0
    seq = [U(i) for i in range(1, 100)]
    for i in range(1, 11):
        op_coeff = np.linalg.solve(M[:i, :i], seq[:i])
        n = i + 1
        while BOP(n, op_coeff) == seq[n]:
            n += 1
        fit += BOP(n, op_coeff) 
        
    print(int(fit))

if __name__ == "__main__":
    main()
