
def big_modulus(base, power, modulus): 
    if base % modulus == 0:
        return 0
    #elif is_prime(p + 1) && m == p:
    #    return 1
    else:
        result = 1
        while power > 0:
            if power % 2 == 1:
                result = (result * base) % modulus
            power = power >> 1
            base = (base * base) % modulus
        return result    
       
total = 0
for i in range(1, 1001):
    total += big_modulus(i, i, 10**10)
print(total % 10**10)
