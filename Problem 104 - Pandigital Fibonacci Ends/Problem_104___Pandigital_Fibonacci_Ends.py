import numpy as np

def pandigital(fib_number):
    one2nine = set("123456789")
    last_digits = str(fib_number % (10**9))
    if set(last_digits) == one2nine:
        first_digits = str(fib_number)[:9]
        if set(first_digits) == one2nine:
            return True
    return False

def main():
    M = np.array([[1, 1],
                  [1, 0]], dtype=object)
    Mpow3 = np.array([[3, 2],
                      [2, 1]], dtype=object)

    n = 1
    while True:
        if pandigital(M[0, 0]): # Ran this shit up to 3.5mil before i realised this was [1, 1]
            print(n + 1)
            break
        
        if pandigital(M[0, 1]):
            print(n + 2)
            break

        if pandigital(M[1, 1]): 
            print(n + 3)
            break
        M = np.matmul(M, Mpow3)
        n += 3

if __name__ == "__main__":
    main()
