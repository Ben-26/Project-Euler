
def main():
    factorial_dict = {0: 1, 1 : 1}
    for i in range(2, 10):
        factorial_dict[i] = i * factorial_dict[i - 1]

    chain_dict = {}
    chains_len_60 = 0
    for i in range(1, 10**6):
        cache = [i]
        while True:
            digit_sum = sum([factorial_dict[int(char)] for char in str(cache[-1])])
            if digit_sum in cache:
                for i, num in enumerate(cache):
                    if num not in chain_dict:
                        chain_dict[num] = len(cache) - i
                break
            cache.append(digit_sum)
            
    for key in chain_dict:
        if chain_dict[key] == 60:
            chains_len_60 += 1
            
    print(chains_len_60)


if __name__ == "__main__":
    main()
