from math import e


def generate_prime_sieve(n):
    bool_primes = [True] * (n + 1)
    bool_primes[0] = bool_primes[1] = False
    for i in range(int(n**0.5) + 1):
        if bool_primes[i]:
            for j in range(i * i, n + 1, i):
                bool_primes[j] = False
                
    primes = [i for (i, is_prime)  in enumerate(bool_primes) if is_prime]
    return primes   

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_right_aligned_triangle_2(triangle, header):
    str_list = []
    for i, h in enumerate(header):
        header[i] = str(h)
        
    for i in range(len(triangle)):
        triangle_str = ""
        for j in range(len(triangle[i])):
            if triangle[i][j]:
                triangle_str += " T " 
            else:
                triangle_str += " _ " 
        str_list.append(triangle_str)
    max_str_len = max([len(s) for s in str_list])
    max_num_len = len(header[-1])
    print(" " * 2 + " ".join(map(str, header)))
    for i, s in enumerate(str_list):
        print(header[i] + " " * (max_str_len - len(s) + max_num_len - len(header[i])) + s)


def main():
    N = 674
    primes = generate_prime_sieve(N) 
    def is_prime(n):
        if n in primes:
            return True
        
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
    
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [3] + primes[3:] # Removing 2 and 5, ending with 2 -> even, ending with 5 -> multiple of 5
    print(primes)

    prime_graph = [[False for _ in range(i)] for i in range(len(primes), 0, -1)]
    

    for i in range(len(primes)):
        for j in range(i + 1, len(primes)): 
            #print(f"{i}, {j}")
            if is_prime(int(str(primes[i]) + str(primes[j]))) and  is_prime(int(str(primes[j]) + str(primes[i]))):
                #print(f"{primes[i]} , {primes[j]}")    
                prime_graph[i][j - i] = True


if __name__ == "__main__":
    main()  
