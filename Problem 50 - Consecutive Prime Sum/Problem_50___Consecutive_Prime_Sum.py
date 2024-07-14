def prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def primeGenerator(max_prime):
    primes = []
    for i in range(2, max_prime):
        if prime(i):
            primes.append(i)
    return primes

def max_count_until_upper_bound(arr, upper_bound):
    n = len(arr)
    max_count = 0
    
    for i in range(n):
        total = arr[i]
        counter = 1  # Start counter at 1 since we're including arr[i]
        
        while i + counter < n and total + arr[i + counter] <= upper_bound:
            total += arr[i + counter]
            counter += 1
        
        max_count = max(max_count, counter)
    
    return max_count

if __name__ == "__main__":
    ub = 10**6
    prime_list = primeGenerator(ub)
    largest_prime = 0
    total_sum = 0
    
    n = len(prime_list)
    max_count = 0
    
    for i in range(n):
        total = prime_list[i]
        counter = 1  # Start counter at 1 since we're including arr[i]
        
        while i + counter < n and total + prime_list[i + counter] <= ub:
            total += prime_list[i + counter]
            counter += 1
            
            if prime(total) and counter > max_count:
                max_count = counter
                largest_prime = total
        
    print(largest_prime)