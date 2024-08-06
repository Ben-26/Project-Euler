from math import log10

def main():
    base_exp = open("0099_base_exp.txt", "r")

    approx = []
    for line in base_exp:
        line = (line.rstrip()).split(",")
        a, b = int(line[0]), int(line[1])
        prod = b * log10(a)
        print(f"Appending {prod}")
        approx.append(prod)
        
    sorted_approx = sorted(approx)
    print(approx.index(sorted_approx[-1]) + 1)


if __name__ == "__main__":
    main()