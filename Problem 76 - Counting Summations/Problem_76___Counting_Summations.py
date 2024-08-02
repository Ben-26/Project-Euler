
def main():
    cache = [0] * 101
    cache[0] = 1

    for i in range(1, 101):
        for j in range(i, 101):
            cache[j] += cache[j - i]

    for i, c in enumerate(cache):
        print(f"{i + 1} can be constructed with {c} combinations")

if __name__ == "__main__":
    main()
    
