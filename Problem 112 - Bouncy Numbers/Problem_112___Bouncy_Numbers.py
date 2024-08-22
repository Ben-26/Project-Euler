def bouncy(n):
    str_n = str(n)
    len_str_n = len(str_n)
    greater, lesser = False, False
    for i in range(1, len_str_n):
        if str_n[i] > str_n[i - 1]:
            greater = True
        if str_n[i] < str_n[i - 1]:
            lesser = True
        if greater and lesser:
            return True
    return False

def main():
    i, num_bouncy = 100, 0
    while num_bouncy / i <= 0.99:
        i += 1
        num_bouncy += bouncy(i)
    
    print(i - 1)

if __name__ == "__main__":
    main()
