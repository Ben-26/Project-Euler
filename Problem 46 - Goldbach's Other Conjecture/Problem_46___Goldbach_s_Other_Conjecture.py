def is_prime(x):
    if (x == 2):
        return True
    if (x < 2 or x % 2 == 0):
        return False
        
    i = 3
    while (i*i <= x):
        if(x % i == 0):
            return False
        i+=2
    return True


for n in range(9, 10000, 2):
    if is_prime(n):
        continue
    solution = True
    
    m = 1
    while(2*m*m < n):
        if is_prime(n - 2*m*m):
            solution = False
            break
        m = m + 1


    if solution:
        print(n)