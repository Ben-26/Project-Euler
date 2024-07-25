def square_digits(x):
    return sum(int(char) ** 2 for char in str(x))

def main():
    n_converges_to = {1: set(), 89: set()}
    cache = {}

    for i in range(1, 10**7):
        current_value = i
        chain = []
        
        while current_value not in n_converges_to and current_value not in cache:
            chain.append(current_value)
            current_value = square_digits(current_value)

        if current_value in cache:
            convergence = cache[current_value]
        else:
            convergence = current_value

        for number in chain:
            cache[number] = convergence

        if convergence == 1:
            n_converges_to[1].add(i)
        else:
            n_converges_to[89].add(i)
    
    print(len(n_converges_to[89]))


if __name__ == "__main__":
    main()
