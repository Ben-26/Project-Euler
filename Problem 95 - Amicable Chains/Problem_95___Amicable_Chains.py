
"""
https://en.wikipedia.org/wiki/Sociable_number
Sol can be found on the wiki page however that is less fun 
"""


def calculate_divisors_in_range(start, end):
    div_dict = {}
    for num in range(start, end + 1):
        divisors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                if i != num // i:
                    divisors.add(num // i)

                if i in div_dict:
                    for d in div_dict[i]:
                        if num % d == 0 and d not in divisors:
                            divisors.add(d)
                if num // i in div_dict:
                    for d in div_dict[num // i]:
                        if num % d == 0 and d not in divisors:
                            divisors.add(d)
        div_dict[num] = sorted(divisors)                    
    return div_dict

def main():
    div_dict = calculate_divisors_in_range(1, 10**6)
    seq_min = float('inf')
    seq_len = 0
    
    for num in div_dict:
        cache = []
        current = num
        
        while True:
            if current == 1 or current >= 10**6:
                break
            if current in cache:
                loop_start = cache.index(current)
                loop = cache[loop_start:]
                
                if loop[0] == num:
                    if len(loop) > seq_len:
                        seq_len = len(loop)
                        seq_min = min(loop)
                    elif len(loop) == seq_len:
                        seq_min = min(seq_min, min(loop))
                break
            cache.append(current)
            current = sum(div_dict[current][:-1]) 
    print(seq_min, seq_len)

if __name__ == "__main__":
    main()