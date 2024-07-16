from math import ceil, log10

if __name__ == "__main__":
    counter = 0
    for a in range(1, 100):
        for n in range(1, 100):
            if len(str(a**n)) == n:
                counter += 1
    print(counter)