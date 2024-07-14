def four_disctinct_prime_factors(n):
    fact = []
    distinct_fact = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fact.append(divisor)
            if divisor not in distinct_fact:
                distinct_fact.append(divisor)
            n //= divisor
        divisor += 1
        if len(distinct_fact) > 4:
            return False
    return (len(distinct_fact) == 4)
   

def has_four_con_elem(arr):
    if len(arr) != 4:
        return False
    elif arr[1] - arr[0] == 1 and arr[2] - arr[1] == 1 and arr[3] - arr[2] == 1:
        return True
    return False

if __name__ == "__main__":
    num_arr = []
    i = 1000
    while not(has_four_con_elem(num_arr)):
        if(four_disctinct_prime_factors(i)):
            num_arr.append(i)
        i += 1
        if len(num_arr) > 4:
            num_arr = num_arr[-4:]
            print(num_arr)
    print(num_arr[0])


